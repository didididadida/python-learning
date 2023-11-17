'''
请编一个程序，用户在同一行内输入两个整数，代表头和脚的数量，编程计算笼中各有多少只鸡和兔，假设鸡和兔都正常，无残疾。如无解则输出Data Error!
a,b = input().split()  #读入两个数到a b中
a,b = map(int,input().split(','))  #读入两个整数到a，b中，输入的数用逗号分隔
a,b = map(int,input().split(' '))  #读入两个整数到a，b中，输入的数用空格分隔
'''
a,b = map(int,input().split(' '))  #读入两个整数到a，b中，输入的数用空格分隔


c = 2 * a
d = b - c
tu = d / 2
ji = a - tu
if ji % 1 == 0 and ji >= 0 and tu >= 0 :

    print(f"{int(ji)} {int(tu)}")
else:
    print('Data Error!')
