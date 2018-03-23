'''
Problem Statement

A postal code P must be a number in the range of (100000-999999).
A postal code P must not contain more than one alternating repetitive digit pair.
Alternating repetitive digits are digits which repeat immediately after the next digit. In other words,
an alternating repetitive digit pair is formed by two equal digits that have just a single digit between them.
'''

import re

P = input().strip()

print(bool(re.search(r'^[1-9]\d{5}$', P) and len(re.findall(r'(?=((\d)\d\2))', P)) <= 1))
