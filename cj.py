#-*-coding:utf-8-*-
def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

n = input("请输入要移动的圆盘数量:")
move(int(n), 'A', 'B', 'C')