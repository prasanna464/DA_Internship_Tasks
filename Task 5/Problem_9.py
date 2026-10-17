# Word Order
# Problem Statement Link :- https://www.hackerrank.com/challenges/word-order/copy-from/485432137

# COde

from collections import Counter

N = int(input())
LIST = []

for i in range(N):
    LIST.append(input().strip())

COUNT = Counter(LIST)

print(len(COUNT))
print(*COUNT.values())
