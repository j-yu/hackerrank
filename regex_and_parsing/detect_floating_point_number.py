'''
Problem Statement

You are given a string N.Your task is to verify that N is a floating point number.
In this task, a valid float number must satisfy all of the following requirements:
>Number can start with +, - or . symbol.
>Number must contain at least one decimal value.
>Number must have exactly one . symbol.
>Number must not give any exceptions when converted using float(N).

Input Format

The first line contains an integer T, the number of test cases.
The next T line(s) contains a string N.
'''

import re

pattern = re.compile(r'(^[+-.]?\d*)(\.\d+$)')

T = int(input())

for N in range(T):
    N = str(input())
    if re.search(pattern, N) is not None:
        print('True')
    else:
        print('False')
