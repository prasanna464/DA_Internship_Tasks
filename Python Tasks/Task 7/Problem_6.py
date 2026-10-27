#  Panagrams
# Problem Statement Link :- https://www.hackerrank.com/challenges/pangrams/problem

# Code

#!/bin/python3

import math
import os
import random
import re
import sys

def pangrams(s):
    letters = set(s.lower())

    if all(char in letters for char in "abcdefghijklmnopqrstuvwxyz"):
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
