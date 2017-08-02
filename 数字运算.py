from functools import reduce
import math

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    b = -1
    a = 0
    for i in s:
        if i == '.':
            a = 1
        if a == 1:
            b = b + 1

