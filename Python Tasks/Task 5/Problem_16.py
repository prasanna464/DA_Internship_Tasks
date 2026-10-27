# Collections.Counter()
# Problem Statement Link :- https://www.hackerrank.com/challenges/collections-counter/copy-from/485432471

# Code

from collections import Counter
numShoes = int(input())
shoes = Counter(map(int, input().split()))
numCust = int(input())

income = 0

for i in range(numCust):
    size, price = map(int, input().split())
    if shoes[size]: 
        income += price
        shoes[size] -= 1
print(income)
