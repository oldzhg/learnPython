# -*- coding: utf-8 -*- 
def triangles():  
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1]                    
n = 1
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
#第一步由列表生成式  range()范围大小是‘L的长度-1’  当L = [1] 时，rang(0)， 则为none，无意义 直接得到[1] + [1]为[1,1]
#第二步，range(1)  取 0 ，内部则为L[0] 和 L[1]相加为2，得到[1,2,1]
#第三步，range（2）取0，1.中间单独循环，得到[3,3],相加后得到[1, 3, 3, 1]
#以此类推，over
