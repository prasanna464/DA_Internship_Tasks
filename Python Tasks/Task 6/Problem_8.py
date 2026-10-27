# Tuples
# Problem Statement Link :- https://www.hackerrank.com/challenges/python-tuples/problem

# Code

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))
