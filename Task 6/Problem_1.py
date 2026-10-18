# Python If-Else
# Problem Statement Link :- https://www.hackerrank.com/challenges/py-if-else/problem

# Code


n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")
