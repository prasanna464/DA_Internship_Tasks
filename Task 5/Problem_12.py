# Capitalize!
# Problem Statement Link :- https://www.hackerrank.com/challenges/capitalize/copy-from/325419976

# Code

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
