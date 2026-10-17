# Set .add()
# Problem Statemnt Link :- https://www.hackerrank.com/challenges/py-set-add/copy-from/328408430


# Code

n = int(input())
NAMES = set([])
for i in range(n):
    NAMES.add(input())
print(len(NAMES))
