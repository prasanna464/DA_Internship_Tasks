# Validating phone numbers

# Problem Statement Link :- https://www.hackerrank.com/challenges/validating-the-phone-number/problem?utm_source=chatgpt.com

# Code

import re
[print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO') for _ in range(int(input()))]
