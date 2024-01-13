'''
杨辉三角形，也称帕斯卡三角，其定义为：顶端是 1,视为(row0).第1行(row1)(1&1)两个1,这两个1是由他们上头左右两数之和 (不在三角形内的数视为0).
依此类推产生第2行(row2):0+1=1;1+1=2;1+0=1.第3行(row3):0+1=1;1+2=3; 2+1=3;1+0=1. 循此法可以产生以下诸行，如下图所示。
定义一个函数 ，传入正整数参数 M，输出 M 行的杨辉三角（为使格式美观，采用M行中最大数的位数 做为数据输出时的占位宽度和 数据间的间隔）。
'''

def triangles(x, y):
    if y == 1 or y == x: # y=1或y=x时，函数返回值为1
        return 1
    else:
        z = triangles(x-1, y-1) + triangles(x-1, y) # y为其他值时的递推公式
        return z
n = int(input())
a = n // 2 + 1
c = len(str(triangles(n, a)))
space = ' ' * c
for i in range(1, n+1): # 输出n行

    for j in range(0, n-i+1):
        print(space, end="")
        c -= j
    for j in range(1, i+1):
        s = triangles(i, j)

        print("%*s" % (len(str(triangles(n, a))),s) + space, end="")

    print()
