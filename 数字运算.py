from functools import reduce
import math

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2float(s):
    def str2int(s):
        return reduce(lambda x, y: x * 10 + y, map(lambda x: d[x], s))

    index = s.find('.')
    if index == -1:
        return str2int(s)
    s = s.replace('.', '')
    return str2int(s) / math.pow(10, len(s) - index)


c = '123.456'
print(str2float(c))
