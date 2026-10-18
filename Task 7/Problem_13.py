# Sherlock and the Valid String 
# Problem Statement Link :- https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

# Code

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def isValid(s):
    freq = Counter(s)
    values = list(freq.values())
    count = Counter(values)

    if len(count) == 1:
        return "YES"

    if len(count) == 2:
        f1, f2 = count.keys()

        if (f1 == 1 and count[f1] == 1) or (f2 == 1 and count[f2] == 1):
            return "YES"

        if abs(f1 - f2) == 1:
            if count[max(f1, f2)] == 1:
                return "YES"

    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
