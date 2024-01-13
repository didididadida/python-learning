"""
请用递归编程实现。
求和 1!+2!+3！…+n！n的值从键盘输入。
"""

def jiecheng(n):
    if n == 1:
        return 1
    else:
        z = n * jiecheng(n-1)
    return z


n = eval(input())
a =0
for i in range(1,n+1):
    a += jiecheng(i)
print(a)