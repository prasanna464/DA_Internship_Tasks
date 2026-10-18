# Set .intersection() Operation
# Problem Statement Link :- https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

# Code

_ = int(input())
SET_N = set(map(int, input().split()))

_ = int(input())
SET_B = set(map(int, input().split()))

print(len(SET_N & SET_B))
