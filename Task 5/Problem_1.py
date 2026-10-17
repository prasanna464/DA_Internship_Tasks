# Find the Runner-Up Score!
# Problem Statement Link :- https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# Code

if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    arr.sort()
    s=set(arr)
    l=list(s)
    print(l[-2])
