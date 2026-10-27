# Write a function
# Problem Statement Link :- https://www.hackerrank.com/challenges/write-a-function/problem

# Code

def is_leap(year):
    leap = False
    leap=(year%400==0) or (year %4==0 and year%100!=0)
    return leap

year = int(input())
print(is_leap(year))
