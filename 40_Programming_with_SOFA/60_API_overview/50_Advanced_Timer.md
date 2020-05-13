Advanced Timer: How to log computation time
===========================================

This is the most precise and flexible way of monitoring the computation
time in SOFA. It prints results on the standard text output. There is an
option in runSofa to activate the display every N time steps from the command line : runSofa --computationTimeSampling N myAmazingScene.pyscn (use
--help for a list of command line options). The parameter update the
variable computationTimeSampling which specifies the intervals (counted
in animation steps) between successive statistics displays. 0 means
deactivated. To monitor the time spent in a specific part of the code,
bracket it as shown below:

`sofa::helper::AdvancedTimer::stepBegin("Build linear equation");`\
`// your code here`\
`sofa::helper::AdvancedTimer::stepEnd("Build linear equation");`

That is all. Then the corresponding computation time can be displayed at
regular intervals. Be careful to use the same string in the two
instructions. The begin/end calls can be nested, to monitor
hierarchically. An example of statistics is shown below. The number of
dots before the name of the piece of code denote the nesting level.

`==== Animate ====`\
\
`Trace of last iteration :`\
` *    0.06 ms > begin Mechanical on Cube grid`\
` *    0.10 ms   > begin Build linear equation`\
` *                > begin forces in the right-hand term`\
` *    1.27 ms     < end   forces in the right-hand term`\
` *    1.37 ms     > begin shift and project independent states`\
` *    1.49 ms     < end   shift and project independent states`\
` *                > begin local M`\
` *    2.11 ms     < end   local M`\
` *    2.38 ms     > begin J products`\
` *   12.89 ms     < end   J products`\
` *   12.91 ms     > begin J products`\
` *   28.06 ms     < end   J products`\
` *                > begin local K`\
` *   28.51 ms     < end   local K`\
` *   28.53 ms     > begin JMJt, JKJt, JCJt`\
` *   86.86 ms     < end   JMJt, JKJt, JCJt`\
` *                > begin implicit equation: scaling and sum of matrices, update right-hand term `\
` *   87.75 ms     < end   implicit equation: scaling and sum of matrices, update right-hand term `\
` *              < end   Build linear equation`\
` *              > begin Solve linear equation`\
` *   90.78 ms   < end   Solve linear equation`\
` *   94.81 ms < end   Mechanical on Cube grid`\
` *   94.83 ms > begin UpdateMapping`\
` *              - step  UpdateMappingEndEvent`\
` *   94.84 ms < end   UpdateMapping`\
` *            > begin UpdateBBox`\
` *   94.93 ms < end   UpdateBBox`\
` *   94.94 ms END`\
\
`Steps Duration Statistics (in ms) :`\
`LEVEL   START    NUM      MIN     MAX   MEAN     DEV    TOTAL  PERCENT ID`\
`  0       0     100      86.57  127.50  109.99    7.77 10999.1  100    TOTAL`\
`  1       0.06    1      86.32  127.25  109.75    7.75  109.75   99.78 .Mechanical`\
`  2       0.09    1      79.42  112.21   99.97    7.02   99.97   90.89 ..Build linear equation`\
`  3       0.09    1       0.84    1.36    1.14    0.14    1.14    1.04 ...forces in the right-hand term`\
`  3       1.34    1       0.07    0.14    0.10    0.02    0.10    0.09 ...shift and project independent states`\
`  3       1.44    1       0.39    0.68    0.55    0.08    0.55    0.50 ...local M`\
`  3       2.23    2       7.52   17.67   12.72    2.34   25.44   23.13 ...J products`\
`  3      27.70    1       0.28    0.54    0.41    0.06    0.41    0.37 ...local K`\
`  3      28.13    1      54.07   79.54   70.61    5.53   70.61   64.20 ...JMJt, JKJt, JCJt`\
`  3      98.75    1       0.88    2.29    1.31    0.24    1.32    1.20 ...implicit equation: scaling and sum of matrices, update right-hand term `\
`  2     100.06    1       2.71    4.79    3.75    0.51    3.75    3.41 ..Solve linear equation`\
`  1     109.84    1       0.01    0.02    0.02    0       0.02    0.01 .UpdateMapping`\
`  2     109.84    1       0       0       0       0       0       0    ..UpdateMappingEndEvent`\
`  1     109.85    1       0.09    0.28    0.14    0.03    0.14    0.12 .UpdateBBox`\
\
`==== END ====`
