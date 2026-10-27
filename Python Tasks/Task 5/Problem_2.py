# String Split and Join
# Problem Statement Link :- https://www.hackerrank.com/challenges/python-string-split-and-join/problem

# Code

def split_and_join(line):
    words = line.split(" ")
    new = "-".join(words)
    return new

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
