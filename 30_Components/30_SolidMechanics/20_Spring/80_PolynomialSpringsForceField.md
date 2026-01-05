PolynomialSpringsForceField
===========================

This component belongs to the category of [ForceField](../../../../simulation-principles/multi-model-representation/forcefield/). This component allows to simulate springs with Polynomial stress strain behavior. If we note:

- $F$ the spring force
- $S$ the cross section (always 1.0)
- $\sigma$ the stress-strain non-linear function
- $l_0$ the original length and $l$ the current length of the spring
- $\Delta u %3D \left\{\begin{matrix} \Delta x\\ \Delta y\\ \Delta z\\ \end{matrix}\right.$ the point displacement

the generic non-linear force can thus be written:

$$
F=S%7E\sigma \left( \frac{l-l_0}{l_0} \right%29 \frac{\Delta u}{l}
$$ 

where $\sigma$ is polynom as follows:

$$
\sigma \left( \frac{l-l_0}{l_0} \right) =\sigma(L)=a_1L+a_2L^2+\cdots+a_nL^n
$$

and

$$
\frac{\partial \sigma}{\partial L}=a_1+a_2L+\cdots+a_nL^{n-1}
$$

The dedication of Jacobian matrix for PolynomialSpringForceField is given below:

$$
J_F(u)=\left(S\frac{\partial \sigma}{\partial L}\cdot\frac{1}{l_0}-S\sigma\cdot\frac{1}{|l|} \right)\begin{bmatrix}\frac{\Delta x^2}{l^2}&\frac{\Delta x\Delta y}{l^2}&\frac{\Delta x\Delta z}{l^2}\\\frac{\Delta y\Delta x}{l^2}&\frac{\Delta y^2}{l^2}&\frac{\Delta y\Delta z}{l^2}\\\frac{\Delta z\Delta x}{l^2}&\frac{\Delta z\Delta y}{l^2}& \frac{\Delta z^2}{l^2}\end{bmatrix} + S\sigma\cdot\frac{1}{|l|}\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}
$$


Note that a **RestShape**PolynomialSpringsForceField does exist. It will compute the same non-linear force with regards to the rest shape of one single object. To avoid Nan problems when a spring has a zero length, an exponential addition to the denominator has been added. As a result, the stress simulation is shifted compared with polynomial values, but it keeps its nonlinearity:

$$
J_F(u)=\left(S\frac{\partial \sigma}{\partial L}\cdot\frac{(1-sc\cdot e^{sh-sc(\Delta x^2 + \Delta y^2 + \Delta z^2)})}{l_0}-S\sigma\cdot\frac{(1-sc\cdot e^{sh-sc(\Delta x^2 + \Delta y^2 + \Delta z^2)})}{\sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2 + e^{sh-sc(\Delta x^2 + \Delta y^2 + \Delta z^2)}}} \right)\cdot\frac{1}{\sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2 + e^{sh-sc(\Delta x^2 + \Delta y^2 + \Delta z^2)}}}\cdot\begin{bmatrix}\Delta x^2&\Delta x\Delta y&\Delta x\Delta z\\\Delta y\Delta x&\Delta y^2&\Delta y\Delta z\\\Delta z\Delta x&\Delta z\Delta y&\Delta z^2\end{bmatrix} + S\sigma\cdot\frac{1}{\sqrt{\Delta x^2 + \Delta y^2 + \Delta z^2 + e^{sh-sc(\Delta x^2 + \Delta y^2 + \Delta z^2)}}}\begin{bmatrix}1&0&0\\0&1&0\\0&0&1\end{bmatrix}
$$

More details were given in the pull-request [#1342](https://github.com/sofa-framework/sofa/pull/1342).


Usage
-----

The PolynomialSpringsForceField **requires** two different objects to link, which means two MechanicalObjects on which the non-linear spring will act.
On the other hand, RestShapePolynomialSpringsForceField will act on one single body, i.e. one MechanicalObject.
