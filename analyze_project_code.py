""" Analyze project code file

"""

import re

import numpy as np


with open('project_code.md', 'rt') as fobj:
    contents = fobj.read()


projects = re.split('^[A-Za-z]+$', contents, flags=re.M)

# Drop heading
projects = projects[1:]

values = []
for project in projects:
    values.append([int(v) for v in project.split()])
values = np.array(values, dtype=float)

test_lines = values[:, 0] - values[:, 1]
