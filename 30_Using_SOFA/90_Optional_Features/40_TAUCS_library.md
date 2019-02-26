Install BLAS/LAPACK library

-   linux : get the version shipped with your distribution
-   mac : ?
-   windows :
    -   Download the precompiled version on :
        <http://www.fi.muni.cz/~xsvobod2/misc/lapack/download/lapack-MT-release.zip>
    -   Extract somewhere and put the \*.lib in
        &lt;SOFA\_DIR&gt;/lib/win32/Common and \*.dll
        &lt;SOFA\_DIR&gt;/bin

Select the following options in CMake:

-   SOFA-EXTERNAL\_HAVE\_METIS
-   SOFA-LIB\_COMPONENT\_TAUCS\_SOLVER

