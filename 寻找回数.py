def cj(n):
    l = str(n)
    return l[::] == l[::-1]

c = input('请输入您寻找的回数范围:')
h = int(c)
for i in range(h):
    x = cj(i)
    if x is True:
        print(i)
