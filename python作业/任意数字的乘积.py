'''
计算任意个输入数字的乘积。
'''
ls = []
ls = input().split(',')

a = 1
for i in range(0,len(ls)):
    a = a * int(ls[i])
print(a)