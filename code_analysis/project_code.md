# Analysis of project code

See `cloc_projects.sh` for source.  Lines are:

* all Python code lines in project (using CLOC utility);
* Python lines minus `tests` directory;
* Python lines minus `tests` directory and `scripts` directory;
* number of detected code statements in coverage;
* percentage of detected code statements covered by tests.
* # PRs
* # Issues

Trying to get a handle on lines of code vs statements.

Project delta `cloc --include-lang=Python code/utils data` (from
`.coveragerc`) -> 302.  212 covered lines. Statements per line = 0.7.

Project epsilon `cloc --include-lang=Python --exclude-dir=tests,scripts
code/utils data` (from `.coveragerc`) -> 392.  352 covered lines.  SPL = 0.90

Project lambda `cloc --include-lang=Python --exclude-dir=tests,scripts code
data` (from `.coveragerc`) -> 732.  693 covered lines.  SPL = 0.95

8 / 11 projects import sklearn. 6 imported statsmodels.  No projects mention
FSL, SPM or AFNI.  One project imported Dipy, to use the brain extraction
code.  2 projects imported nilearn, in both cases they used smoothing, and
visualization.  1 project imported nitime.

Alpha

3885
3293
1910
180
68
190
27

Beta

2296
1753
1753
36
97
147
13

Delta

1299
966
302
212
100
122
37

Epsilon

2289
1809
392
352
100
310
31

Eta

624
588
588
75
97
89
17

Gamma

1494
1040
1040
392
100
79
12

Iota

964
928
928
79
99
113
31

Kappa

1194
1157
1157
42
95
99
37

Lambda

1172
732
732
693
97
67
27

Theta

1653
1186
431
277
99
113
28

Zeta

8582
8287
8287
541
96
49
4
