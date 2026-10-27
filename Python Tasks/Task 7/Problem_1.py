# Set symmetric_difference() Operation

# Pronlem Statement Link :- https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/copy-from/328540706

# Code

_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

print(len(SET_N.symmetric_difference(SET_B)))
