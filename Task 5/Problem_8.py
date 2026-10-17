# Set .add()
# Problem Statement Link :- https://www.hackerrank.com/challenges/py-set-add/problem

# COde

n = int(input())
NAMES = set([])
for i in range(n):
    NAMES.add(input())
print(len(NAMES))
