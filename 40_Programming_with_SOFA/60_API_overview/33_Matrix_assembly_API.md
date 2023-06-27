Matrix Assembly API
===

To overcome several limitations of SOFA, it has been decided to refactor the linear system assembly in SOFA. This document describes the former limitations as well as the new API and the associated refactoring.

This work is now available in SOFA since [SOFA v23.06](https://www.sofa-framework.org/about/sofa-v23-06/).


## Limitations in SOFA v22.12

- No direct access to system matrices (MBK) for users. Some users may want to extract the matrix of a specific force field (local to an object) for analyzing it, or even to modify it with an external tool (python, matlab etc).
- Steep learning curve for newcomers. It is quite complex to understand how to implement a new component, such as a force field. It is not obvious how the matrices are created and computed, or if the matrix system is not built. In that later case, how does it work?
- It is difficult to understand the difference between addDForce and addKtoMatrix. They both are related to the derivative of the force which indicates that they could probably be reunited. A reunification would be less error-prone.
- Currently, constraints are solved in an indirect fashion: a free motion step followed by a correction. A direct solver would require to build a matrix system embedding the constraints. This is not considered with the current implementation, but could be in the future.
- Mapping of non-constant forces does not work for solvers assembling their matrices. A workaround is to use the famous component MechanicalMatrixMapper. This component is required for simulations where the matrix is assembled, but not for matrix-free.
- Geometric stiffness of non-linear mappings are not considered. A workaround is to use the component MappingGeometricStiffnessForceField, but not for matrix-free.
- The type of the global system matrix is chosen by the template type of the linear solver. It is not clear for the user that this template has an effect till the force field.
- The type of matrix is imposed to the force field → difficult to optimize. Currently, some force fields perform different operations based on the type of the passed matrix, which is checked with a dynamic cast. Optimizing the matrix assembly should not be up to the force fields.
- Difficult to integrate matrix solvers libraries (e.g. eigen, pardiso etc).
- Unnecessary copies in constraint solving
- A force field or a mass can have access to the entire global matrix: dangerous

## SofaMatrix Plugin

A plugin has been introduced to answer some limitations through additional SOFA components, without any change in SOFA.

See the [readme file](https://github.com/sofa-framework/sofa/blob/master/applications/plugins/SofaMatrix/SofaMatrix.md) for a detailed introduction of SofaMatrix.

To summarize,`GlobalSystemMatrixExporter` is useful to analyze the global system matrix, and `GlobalSystemMatrixImage` is a user-friendly way to visualize the system matrix directly into the Qt-based GUI of runSofa.

## Python Bindings

Python bindings have been introduced to be able to extract some matrices and vectors during a simulation:
- Global system matrix
- Global system right-hand side
- Global system solution
- Mass matrix
- Stiffness matrix
- Compliance matrix projected in the constraint space

```python=
# Get the global system matrix from the linear solver
system_matrix = root.linear_solver.A()

# Get the RHS vector from the linear solver
rhs = root.linear_solver.b()

# Get the solution vector from the linear solver
solution = root.linear_solver.x()

# Assemble the mass matrix from the mass component
mass_matrix = root.mass.assembleMMatrix()

# Assemble the stiffness matrix from the force field component
stiffness_matrix = root.force_field.assembleKMatrix()

# Get the constraint matrix from the constraint solver
compliance_matrix = root.constraint_solver.W()
```

## Reminders

### Global Matrix Contributors

The following components contributes to the global matrix:
- Force fields
- Masses
- Projective constraints
- Non-linear mappings

### addKToMatrix

`BaseForceField::addKToMatrix` and `BaseForceField::addBToMatrix` are the functions where the contributions from a force field to the global system matrix are added.
They corresponds respectively to the derivative of the force with respect to the position (stiffness), and the derivative of the force with respect to the velocity (damping).
There is an equivalent function for masses: `BaseMass::addMToMatrix`.

Signature of the `BaseForceField::addKToMatrix` function:

```cpp
void addKToMatrix(const MechanicalParams* mparams, const sofa::core::behavior::MultiMatrixAccessor* matrix );
```

Signature of the `BaseForceField::addBToMatrix` function:

```cpp
void addBToMatrix(const MechanicalParams* mparams, const sofa::core::behavior::MultiMatrixAccessor* matrix );
```

Signature of the `BaseMass::addMToMatrix` function:

```cpp
void addMToMatrix(const MechanicalParams* mparams, const sofa::core::behavior::MultiMatrixAccessor* matrix)
```


A challenge for the user is to understand both parameters.

In `ForceField`, an overload of the function `addKToMatrix` is introduced with the following parameters

```cpp
void addKToMatrix(sofa::linearalgebra::BaseMatrix * matrix, SReal kFact, unsigned int &offset)
```

The overload of the function `addBToMatrix` is:
```cpp
void addBToMatrix(sofa::linearalgebra::BaseMatrix * matrix, SReal bFact, unsigned int &offset)
```

While in `Mass`, the overload is:

```cpp
void addMToMatrix(sofa::linearalgebra::BaseMatrix * matrix, SReal mFact, unsigned int &offset)
```

The following questions rise:
- What is `kFact`, `bFact` and `mFact`? What should the developer do with it?
- What is `offset`? What should the developer do with it?


As a reminder:
- `kFact`, `bFact` and `mFact` are coefficients to multiply to, respectively, the stiffness matrix, the damping matrix and the mass matrix. Those coefficients come from the ODE solver. They are crucial for a simulation to work. In other words, it is required that the developper multiply each matrix coefficient by one of those factors.
- `offset` is an index to where the force field or mass must start adding its contribution into the global matrix. Its value depends on the mechanical state the component is associated to.

Now that we have answered the questions, we can observe that it is very easy for a developer to:
- Forget to use the `kFact`, `mFact` and `offset`
- Introduce errors by a wrong usage of the `kFact`, `mFact` and `offset`
- Introduce errors by adding contributions at the wrong location in the matrix

### Compressed Sparse Row

Compressed sparse row is a data structure representing a sparse matrix.
In SOFA, the type is `CompressedRowSparseMatrix` and derives from `BaseMatrix`.
Its main template parameter is the type of blocks stored in the data structure.
In SOFA, `CompressedRowSparseMatrix` is often templated with a scalar or with a 3x3 block `sofa::type::Mat<3,3,Real>`.

## Block-based Optimizations

In `BaseForceField::addKToMatrix`, the force field can have access to a `sofa::linearalgebra::BaseMatrix`, which is a pointer to the global matrix system. The type of the matrix is not known (`BaseMatrix` is an interface, a base class for matrix types).

The matrix assembly can be made faster for types `CompressedRowSparseMatrix<sofa::type::Mat<3,3,Real>`, compared to `CompressedRowSparseMatrix<Real>`. This is due to the reduction of searches in the structure when a contribution is added.

However, the speed up was not transparent. The function to call for this optimization was in the class `CompressedRowSparseMatrix` and not in its base class `BaseMatrix`. Therefore, force fields, which have access to a `BaseMatrix` could not benefits from this optimization. A workaround was to test the type of `BaseMatrix` with a `dynamic_cast` in the force field. Therefore, it was the responsability of the force field to test the type of matrix. This responsability was taken by only a few force fields. This test also made the `addKToMatrix` function more complex, introducing branches depending on the type of matrix. See an example in `TetrahedronFEMForceField` from SOFA v20.12: https://github.com/sofa-framework/sofa/blob/v20.12/SofaKernel/modules/SofaSimpleFem/src/SofaSimpleFem/TetrahedronFEMForceField.inl#L1996

```cpp
if (sofa::component::linearsolver::CompressedRowSparseMatrix<defaulttype::Mat<3,3,double> > * crsmat = dynamic_cast<sofa::component::linearsolver::CompressedRowSparseMatrix<defaulttype::Mat<3,3,double> > * >(mat))
{
    for(it = _indexedElements->begin(), IT=0 ; it != _indexedElements->end() ; ++it,++IT)
    {...}
}
else if (sofa::component::linearsolver::CompressedRowSparseMatrix<defaulttype::Mat<3,3,float> > * crsmat = dynamic_cast<sofa::component::linearsolver::CompressedRowSparseMatrix<defaulttype::Mat<3,3,float> > * >(mat))
{
    for(it = _indexedElements->begin(), IT=0 ; it != _indexedElements->end() ; ++it,++IT)
    {...}
}
else
{...}
```

In the pull request [#2281](https://github.com/sofa-framework/sofa/pull/2281), a template specialization of the `add` function for blocks of 3x3 is introduced. Instead to call 9 times the `add` function on scalars, it directly insert the blocks of 3x3. This is exactly what was missing to transparently making the insertion of 3x3 blocks efficient.

Since this introduction, it is not required to test the type of matrix in the force field. The content of `addKToMatrix` should be simplified by removing the branches. It is also homogenous through all the force fields.

This optimization was a step toward the simplification the API of matrix assembly.

## Refactoring

This section is a detailed description of the main changes in SOFA in order to address the current limitations. Those changes are not additions, such as in SofaMatrix plugin, but really changes that will affect both the developers and the users. Most of those changes are introduced in the pull request [#2777](https://github.com/sofa-framework/sofa/pull/2777/).

### Specifications

Minimal impact on the current simulation scenes:
- Current simulation scenes should be able to be loaded and run properly
- If any change in the scene is required but yet supported by the new design, a message warns the user
- It is possible to assemble more than one global matrix: for example, it should be possible to assemble the usual global matrix (weighted sum of mass matrix, damping matrix and stiffness matrix), but also other matrices, such as the mass matrix or the stiffness matrix stored independently from the global matrix.
- Scenes with more than one linear solver in the same Node must be supported. It is the case when a preconditioned conjugate gradient is used.
- SofaCUDA plugin must be supported.
- Impacts on the developpers (API changes) must be detailed to ease the transition.

New features:
- Matrix mapping is possible
- All components that can have a contribution to the global matrix must be supported. In particular non-linear mappings which was not the case before.

### Uncoupling of Linear System and Linear Solver

In SOFA, linear solvers are components that have several responsabilities:
- Storing the linear system
- Assembling the linear system (when the system is assembled)
- Inverting and solving the linear system
- Using the factorization for other purposes: multiplication of the inverse of the global matrix with the transpose of the compliance matrix.

To comply with the [*Single-responsibility principle*](https://en.wikipedia.org/wiki/Single-responsibility_principle), a new type of component is introduced: Linear System. The responsabilities of storing and assembling the linear system are transfered from the LinearSolver to the LinearSystem. Actually, storing and managing memory for the linear system is also done in another class but it is encapsulated in the Linear System component.

Previously, SOFA did not automatically support the assembly of mapped components. This issue needed to be addressed, but it dramatically increased the complexity of the matrix assembly method. It is another reason to separate assembly and solving.

To summarize, the old LinearSolver is now a combination of a LinearSystem with a new lighter LinearSolver.


#### Scene Design

Due to the previous reason, the Nodes containing a LinearSolver in the SOFA scenes should now have 2 components: a LinearSystem and a LinearSolver.

For example,

```xml
<EulerImplicitSolver/>
<SparseLDLSolver/>
```

should now be written:

```xml
<EulerImplicitSolver/>
<MatrixLinearSystem name="system"/>
<SparseLDLSolver linearSystem="@system"/>
```

Note that the component `MatrixLinearSystem` is a component LinearSystem and will be introduced in details later.

##### Backward compatibility

In order not to break scenes which were written with only a linear solver and without a linear system, SOFA will automatically create a linear system if none is found in the current context of the linear solver. Therefore, the changes introduced with the addition of a new component should not break the old scenes. Nevertheless, a message will warn the user to add a linear system component in the scene.

The SOFA scenes shipped with the source code will be updated according to the new design.


#### Architecture

The linear system components all derive from a base abstract class `sofa::core::behavior::BaseMatrixLinearSystem`. An intermediate templated class `sofa::component::linearsolver::linearsystem::MatrixLinearSystem` deriving from `BaseMatrixLinearSystem` is in charge of storing the linear system as a matrix and two vectors (the right hand side of the system and the solution).

#### Interaction between Linear System and Linear Solver


In the simple cases, only one linear system and one linear solver are defined:

```xml
<EulerImplicitSolver/>
<MatrixLinearSystem name="system"/>
<SparseLDLSolver linearSystem="@system"/>
```

However, more complex scenarios must be supported:

- **Multiple assembled matrices**: 

```xml
<EulerImplicitSolver/>

<Node name="matrices">
    <MatrixLinearSystem name="system"/>
    <MatrixLinearSystem name="K" assembleMass="false" assembleMappings="false" applyProjectiveConstraints="false"/>
    <MatrixLinearSystem name="M" assembleStiffness="false" assembleMappings="false" applyProjectiveConstraints="false"/>
</Node>
<CompositeLinearSystem name="solverSystem" linearSystems="@matrices/system @matrices/K @matrices/M" solverLinearSystem="@system"/>

<SparseLDLSolver linearSystem="@solverSystem"/>
```

In this scenario, the user wants to assemble the stiffness matrix and the mass matrix independently from the global matrix, and access it in a component.

- **Preconditioners**:

If preconditioners are used along with a `ShewchukPCGLinearSolver`, the scene may look like:

```xml
<ShewchukPCGLinearSolver name="PCG" iterations="1000" preconditioners="preconditioner"/>
<WarpPreconditioner name="preconditioner" solverName="initSolver" printLog="true"/>
<SparseLDLSolver name="initSolver" template="CompressedRowSparseMatrixMat3x3d" />
```

In this example, three linear solvers can be found inside the same context. 

Due to the uncoupling of the linear system from the linear solver, a linear system must be associated to each one of the solver. Which means 6 components instead of 3. It would look like:

```xml
<MatrixFreeSystem name="mainSystem"/>
<ShewchukPCGLinearSolver name="PCG" iterations="1000" preconditioners="preconditioner" linearSystem="@mainSystem"/>

<RotationMatrixSystem name="rotation"/>
<WarpPreconditioner name="preconditioner" solverName="initSolver" printLog="true" linearSystem="@rotation"/>

<MatrixLinearSystem name="initSystem" template="CompressedRowSparseMatrixMat3x3d"/>
<SparseLDLSolver name="initSolver" template="CompressedRowSparseMatrixMat3x3d" linearSystem="@initSystem"/>
```

There are three linear systems in the same context. The situation is similar to the previous example, where the user wants to assemble matrices independently. However, the nature of the matrices are different, and they should not be assembled with the same method. For example, the linear system `initSystem` must be assembled only at the initialization stage, not at each time step.


#### Multiple Assembled Matrices

The extraction of the linear system from the linear solver allows to formulate the matrix assembly with different algorithms through different components.
In the proposed changes, a linear system component is introduced: `MatrixLinearSystem`, a default component able to store and assembly any linear system type.


### API Changes

#### Simplifications through an Interface

One of the difficulties related to the previous implementation was the use of the class `sofa::core::behavior::MultiMatrixAccessor`. Its type name was not explicit on its functionalities, and it lacked documentation. And yet, it is crucial to use it properly when implementing `addKToMatrix`, `addBToMatrix` or `addMToMatrix`.

Usually, a `sofa::linearalgebra::BaseMatrix` is accessed in order to add contributions into it through the `BaseMatrix::add` functions.

The new design keeps the same principle of calling `add` functions, but using an interface instead, not through a `BaseMatrix`. That is why, the class `sofa::core::MatrixAccumulator` is introduced. It is a simple interface, designed to customize the matrix assembly in derived classes.

Here is the implementation of the `MatrixAccumulator` class:

```cpp=
class SOFA_CORE_API MatrixAccumulatorInterface
{
public:
    virtual ~MatrixAccumulatorInterface() = default;

    virtual void add(sofa::SignedIndex /*row*/, sofa::SignedIndex /*col*/, float /*value*/) {}
    virtual void add(sofa::SignedIndex /*row*/, sofa::SignedIndex /*col*/, double /*value*/) {}

    virtual void add(sofa::SignedIndex row, sofa::SignedIndex col, const sofa::type::Mat<1, 1, float> & value);
    virtual void add(sofa::SignedIndex row, sofa::SignedIndex col, const sofa::type::Mat<1, 1, double>& value);
    virtual void add(sofa::SignedIndex row, sofa::SignedIndex col, const sofa::type::Mat<2, 2, float> & value);
    virtual void add(sofa::SignedIndex row, sofa::SignedIndex col, const sofa::type::Mat<2, 2, double>& value);
    virtual void add(sofa::SignedIndex row, sofa::SignedIndex col, const sofa::type::Mat<3, 3, float> & value);
    virtual void add(sofa::SignedIndex row, sofa::SignedIndex col, const sofa::type::Mat<3, 3, double>& value);

    virtual void clear() {}
};
```

This class is essential in the new design. It replaces all the parameters provided to `addKToMatrix`: `MultiMatrixAccessor`, `BaseMatrix`, offset, factor.


#### Index Checking

When a component will use the interface, through the `add` method, it can pass any value for `row` and `col`. In particular, if the code is buggy, the values for `row` and `col` can be out of the matrix bounds, or not in the submatrix associated to the component.

Therefore, an index checking strategy has been implemented. The idea is to inherit from `MatrixAccumulatorInterface` and check indices in the `add` methods. To do that, a helper class is available: `MatrixAccumulatorIndexChecker`. Its two template parameters are:
1. `TBaseMatrixAccumulator`: a type derived from `MatrixAccumulatorInterface`
2. `TStrategy`: the type of strategy to check indices. The strategy can be `NoIndexVerification` or `RangeVerification`. More strategies can be added in the future.

The matrix accumulators used in `MatrixLinearSystem` use this class. A boolean `Data` in `MatrixLinearSystem` defines if the strategy to instantiate is `NoIndexVerification` or `RangeVerification`. By default, index checking is disabled for performances reasons. Nevertheless, note that index checking has only a small consequence on the performances.

#### Mass

In masses, the new design replaces the `addMToMatrix` function by the following function:

```cpp
void buildMassMatrix(MassMatrixAccumulator* matrices);
```

This function is introduced in `sofa::core::behavior::BaseMass`. No overload is available to reduce the complexity.

`MassMatrixAccumulator` is a direct derived class of `sofa::core::MatrixAccumulatorInterface`, but still an interface. It is a strong type to make the interface clearer: this `MatrixAccumulatorInterface` is dedicated to masses, and cannot be passed to any other function taking strong-typed `MatrixAccumulatorInterface`.

In the previous design, a factor needed to be introduced to multiply it by the matrix contribution prior to add the contribution into the global matrix. It is no longer necessary: the matrix assembly method implemented in a LinearSystem component is now responsible to manage the factors.


#### Force Fields

In force fields, the new design replaces the `addKToMatrix` function by the following function:

```cpp
void buildStiffnessMatrix(StiffnessMatrix* matrix);
```

This function is introduced in `sofa::core::behavior::BaseForceField`. No overload is available to reduce the complexity.

`StiffnessMatrix` is a type containing several `MatrixAccumulatorInterface`'s. Contrary to a mass, there is an additional step to access the right `MatrixAccumulatorInterface`. This is mainly to support `InteractionForceField`'s, where the component deals with more than one mechanical state.

The `addBToMatrix` function is replaced by:

```cpp
void buildDampingMatrix(DampingMatrix* matrix)
```

`DampingMatrix` is a type containing several `MatrixAccumulatorInterface`'s.

In the previous design, a factor needed to be introduced to multiply it by the matrix contribution prior to add the contribution into the global matrix. It is no longer necessary: the matrix assembly method implemented in a LinearSystem component is now responsible to manage the factors.

##### Example

The following code snippet is the `addKToMatrix` function from the `HexahedronFEMForceField` in SOFA v21.12 ([link to the code](https://github.com/sofa-framework/sofa/blob/d300cc9af550afbd5c2167470676a5a7d47381a1/SofaKernel/modules/SofaSimpleFem/src/SofaSimpleFem/HexahedronFEMForceField.inl#L1130))

```cpp=
template<class DataTypes>
void HexahedronFEMForceField<DataTypes>::addKToMatrix(const core::MechanicalParams* mparams, const sofa::core::behavior::MultiMatrixAccessor* matrix)
{
    // Build Matrix Block for this ForceField

    sofa::core::behavior::MultiMatrixAccessor::MatrixRef r = matrix->getMatrix(this->mstate);
    const Real kFactor = (Real)sofa::core::mechanicalparams::kFactorIncludingRayleighDamping(mparams, this->rayleighStiffness.getValue());

    sofa::Index e { 0 }; //index of the element in the topology

    const auto& stiffnesses = _elementStiffnesses.getValue();
    const auto* indexedElements = this->getIndexedElements();

    for (const auto& element : *indexedElements)
    {
        const ElementStiffness &Ke = stiffnesses[e];
        const Transformation Rot = getElementRotation(e);
        e++;

        // find index of node 1
        for (Element::size_type n1 = 0; n1 < Element::size(); n1++)
        {
            const auto node1 = element[n1];
            // find index of node 2
            for (Element::size_type n2 = 0; n2 < Element::size(); n2++)
            {
                const auto node2 = element[n2];

                const Mat33 tmp = Rot.multTranspose( Mat33(
                        Coord(Ke[3*n1+0][3*n2+0],Ke[3*n1+0][3*n2+1],Ke[3*n1+0][3*n2+2]),
                        Coord(Ke[3*n1+1][3*n2+0],Ke[3*n1+1][3*n2+1],Ke[3*n1+1][3*n2+2]),
                        Coord(Ke[3*n1+2][3*n2+0],Ke[3*n1+2][3*n2+1],Ke[3*n1+2][3*n2+2])) ) * Rot;

                r.matrix->add( r.offset + 3 * node1, r.offset + 3 * node2, tmp * (-kFactor));
            }
        }
    }
}
```

Due to the API changes, the new function `buildStiffnessMatrix` looks like:

```cpp=
template<class DataTypes>
void HexahedronFEMForceField<DataTypes>::buildStiffnessMatrix(core::behavior::StiffnessMatrix* matrix)
{
    sofa::Index e { 0 }; //index of the element in the topology

    const auto& stiffnesses = _elementStiffnesses.getValue();
    const auto* indexedElements = this->getIndexedElements();

    auto dfdx = matrix->getForceDerivativeIn(this->mstate.get())
                       .withRespectToPositionsIn(this->mstate.get());

    for (const auto& element : *indexedElements)
    {
        const ElementStiffness &Ke = stiffnesses[e];
        const Transformation& Rot = getElementRotation(e);
        e++;

        for (Element::size_type n1 = 0; n1 < Element::size(); n1++)
        {
            const auto node1 = element[n1];
            for (Element::size_type n2 = 0; n2 < Element::size(); n2++)
            {
                const auto node2 = element[n2];

                const Mat33 tmp = Rot.multTranspose( Mat33(
                        Coord(Ke[3*n1+0][3*n2+0],Ke[3*n1+0][3*n2+1],Ke[3*n1+0][3*n2+2]),
                        Coord(Ke[3*n1+1][3*n2+0],Ke[3*n1+1][3*n2+1],Ke[3*n1+1][3*n2+2]),
                        Coord(Ke[3*n1+2][3*n2+0],Ke[3*n1+2][3*n2+1],Ke[3*n1+2][3*n2+2])) ) * Rot;

                dfdx(3 * node1, 3 * node2) += - tmp;
            }
        }
    }
}
```

It can be observed that the function content is very similar at the exception that:

- `offset` and `kFactor` variables disappeared
- the API clearly states that the function deals with the derivative of the force with respect to the position. It also states clearly to which mechanical states the force is computed. It is particularly useful for `InteractionForceField`'s.
- the API looks more to a mathematical formulation: `dfdx(3 * node1, 3 * node2) += - tmp`

The approach is similar for damping, except that the derivative is with respect to the velocity:

```cpp
template <class DataTypes>
void UniformVelocityDampingForceField<DataTypes>::buildDampingMatrix(core::behavior::DampingMatrix* matrix)
{
    if( !d_implicit.getValue() ) return;

    auto dfdv = matrix->getForceDerivativeIn(this->mstate)
                       .withRespectToVelocityIn(this->mstate);

    const sofa::Size size = this->mstate->getMatrixSize();
    const auto damping = sofa::helper::ReadAccessor(dampingCoefficient);
    for( sofa::Size i = 0; i < size; ++i)
    {
        dfdv(i, i) += -damping.ref();
    }
}
```

#### InteractionForceField

`InteractionForceField` is very similar to `ForceField` except is can deal with multiple mechanical states. Here is an example from `StiffSpringForceField`:

```cpp
auto df1_dx1 = matrix->getForceDerivativeIn(m1).withRespectToPositionsIn(m1);
auto df1_dx2 = matrix->getForceDerivativeIn(m1).withRespectToPositionsIn(m2);
auto df2_dx1 = matrix->getForceDerivativeIn(m2).withRespectToPositionsIn(m1);
auto df2_dx2 = matrix->getForceDerivativeIn(m2).withRespectToPositionsIn(m2);

for (sofa::Index e = 0; e < n; ++e)
{
    const Spring& s = ss[e];
    const Mat& m = this->dfdx[e];

    const unsigned p1 = Deriv::total_size * s.m1;
    const unsigned p2 = Deriv::total_size * s.m2;

    df1_dx1(p1, p1) += -m;
    df1_dx2(p1, p2) +=  m;
    df2_dx1(p2, p1) +=  m;
    df2_dx2(p2, p2) += -m;
}
```


#### Projective Constraints

Similarly to force fields and masses, an interface is introduced: `sofa::core::behavior::ZeroDirichletCondition`. 

```cpp=
/**
 * Interface to apply a zero Dirichlet boundary condition on a matrix
 *
 * If K is a matrix to apply a zero Dirichlet boundary condition:
 *  K_ii = 1
 *  K_ij = 0 for i != j
 *  K_ji = 0 for i != j
 */
struct ZeroDirichletCondition
{
    virtual ~ZeroDirichletCondition() = default;
    /**
     * Zero out a row and a column of a matrix. The element at the
     * intersection of the row and the column is set to 1.
     */
    virtual void discardRowCol(sofa::Index /*row*/, sofa::Index /*col*/) {}
};
```

The following function is introduced in projective constraints:

```cpp
void applyConstraint(sofa::core::behavior::ZeroDirichletCondition* /*matrix*/) {}
```

Projective constraints have to implement this function and specify where in the matrix the constraints apply.

#### Non-linear Mappings

Similarly to force fields and masses, an interface is introduced: `MappingMatrixAccumulator`.

A function is introduced to call the matrix accumulation:

```cpp
void buildGeometricStiffnessMatrix(sofa::core::MappingMatrixAccumulator* matrices);
```

Mappings (linear and non-linear) already have a function `getK` to compute their contribution to the global matrix. This function is used to add its contributions into the global matrix. Direct accumulation, without the function `getK`, can be considered in the future.

### Multiple Methods of Matrix Assembly

Uncoupling the linear system and the linear solver allows to implement multiple methods for matrix assembly, and still using the same desired solver. The scene designer can select which method is best suited for the problem to solve. Any solver can then be associated to the selected linear system.

#### MatrixLinearSystem

`MatrixLinearSystem` can be considered as the default matrix assembly method. It supports contributions from force fields, masses, non-linear mappings and projective constraints. It also supports matrix mapping.

#### CompositeLinearSystem

`CompositeLinearSystem` is a component to use if the user wants to assemble more than one matrix. For example, the user may want to assemble the global matrix and solve it with the linear solver, but also the stiffness matrix to analyze it.

```xml
<Node name="matrices">
    <MatrixLinearSystem template="CompressedRowSparseMatrixd" name="system"/>
    <MatrixLinearSystem template="CompressedRowSparseMatrixd" name="K" assembleMass="false" assembleMappings="false" applyProjectiveConstraints="false"/>
    <MatrixLinearSystem template="CompressedRowSparseMatrixd" name="M" assembleStiffness="false" assembleMappings="false" applyProjectiveConstraints="false"/>
</Node>
<CompositeLinearSystem template="CompressedRowSparseMatrixd" name="solverSystem" linearSystems="@matrices/system @matrices/K @matrices/M" solverLinearSystem="@matrices/system"/>
<SparseLDLSolver template="CompressedRowSparseMatrixd" linearSystem="@solverSystem"/>
```

### Matrix Mapping

Matrix mapping is one of the feature that was missing in SOFA, despite its crucial importance. It led to the development of the component MechanicalMatrixMapper, which must be added in the scene to map matrices. However, it is not obvious for the user why this component must be added. Moreover, matrix-free solvers do not need this component leading to an inconsistency between matrix-free methods and assembled methods. Matrix mapping must be managed automatically, without any intervention from the user.

Previously, mapped components could not contribute to the global matrix. In this refactoring, similarly to non-mapped components, mapped components contribute to a matrix, but not the global one. They have their own mapped matrix. Once the mapped matrix is assembled, the matrix is then projected onto the global matrix.

To make this process automatic, the local matrices of mapped and non-mapped components have a different behavior. A mapped component will not have the same local matrix than a non-mapped component. Therefore, it is crucial to know if a component is mapped or not. To this end, the mapping graph is introduced.

#### Mapping Graph

Traditionally in SOFA, methods rely on the scene graph. Here, the matrix assembly relies on the mapping graph. Before assembling the matrices, the mapping graph is built. It builts relationships between components based on their relationships with a mechanical object and a mapping.

The mapping graph finds all the mappings, and their associated mechanical object. It is then known which mechanical objects are considered "main", and which ones are mapped.
Then, the mapping graph finds all components associated to a mechanical object, so it is known which components are mapped or non-mapped.

### Deprecation


MappingGeometricStiffnessForceField and MechanicalMatrixMapper are deprecated, because their purpose is now included natively in the matrix assembly component.


## Local Matrices

Once the LinearSystem has analyzed the mapping graph, it will associate a local matrix to all contributors of the global matrix. Local matrices are BaseObject deriving from `MatrixAccumulatorInterface`. They are added as slave to objects they are associated to.

To be more precise, the local matrices associated to force fields derive from `StiffnessMatrixAccumulator`. Similarly, the local matrices assocaited to masses derive from `MassMatrixAccumulator`, so they are compatible with `void BaseMass::buildMassMatrix(sofa::core::behavior::MassMatrixAccumulator* matrices)`. Mappings also have local matrices: they derive from `MappingMatrixAccumulator` and are compatible with `void BaseMapping::buildGeometricStiffnessMatrix(sofa::core::MappingMatrixAccumulator* matrices)`.

Local matrices have the responsability to receive the contributions from the components (force fields, masses and mappings) and add them in the global matrix. As mentionned earlier, mapped components don't add their contributions directly in the global matrix. An intermediate matrix is assembled, then projected into the global matrix. This difference of behavior between mapped and non-mapped components is solved by different local matrix components. The local matrices associated to main (non-mapped) components add the contributions directly into the global matrix. The local matrices associated to mapped component add the contributions to the intermediate matrix.

## Backward compatibility

A new API has been introduced. It is important that all components are updated according to this new API. Nevertheless, a compatibility layer has been introduced to make the bridge between the new API and the old one. Therefore, components written with the old API should work as expected.

If your version of SOFA has been compiled using the CMake option `-DSOFA_WITH_DEVTOOLS=ON`, you will then receive in your simulation a warning from components which are not yet using the new API. The warning would look like:

```
[WARNING] [YourForceField(YourForceField)] buildStiffnessMatrix not implemented: for compatibility reason, the deprecated API (addKToMatrix) will be used. This compatibility will disapear in the future, and will cause issues in simulations. Please update the code of YourForceField to ensure right behavior: the function addKToMatrix has been replaced by buildStiffnessMatrix
[WARNING] [YourForceField(YourForceField)] buildDampingMatrix not implemented: for compatibility reason, the deprecated API (addBToMatrix) will be used. This compatibility will disapear in the future, and will cause issues in simulations. Please update the code of YourForceField to ensure right behavior: the function addBToMatrix has been replaced by buildDampingMatrix
[WARNING] [YourMass(YourMass)] buildMassMatrix not implemented: for compatibility reason, the deprecated API (addMToMatrix) will be used. This compatibility will disapear in the future, and will cause issues in simulations. Please update the code of YourMass to ensure right behavior: the function addMToMatrix has been replaced by buildMassMatrix
```


## Conclusion and future work


Features that are mentioned in this document are not yet available:
- The SOFA scenes shipped with the source code will be updated according to the new design.
- `ConstantSparsityPatternSystem` has been experimented but is not shipped in [#2777](https://github.com/sofa-framework/sofa/pull/2777). It needs to be introduced again in a later pull request.
- Is it possible to merge the two cases in `InteractionForceField` (mstate1 == mstate2)?


With the refactoring, there are opportunities to use multithreading to speed up matrix assembly:
- Mapped components and non-mapped components add their contributions in different matrices (the global matrix for non-mapped component and an intermediate matrix for mapped components). Since they are independant data structures, they can be assembled concurrently.
- Asynchronous add: assembling the data structure of the matrix takes some time. We propose to deport this time in another thread.
