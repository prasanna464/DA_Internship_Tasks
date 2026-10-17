# String Validators
# Problem Statement Link :- https://www.hackerrank.com/challenges/string-validators/problem

# Code

if __name__ == '__main__':
    s = input()
    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))
