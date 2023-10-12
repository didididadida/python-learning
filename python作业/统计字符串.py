"""
问题描述】统计一行字符的大写字母，小写字母和数字的个数。先输出大写字母个数，在输出小写字母个数，最后输出数字个数。
【输入形式】ljaij1A
【输出形式】1

                        5

                        1
【提示】用字符串的方法isupper, islower来判别大小写。isdigit来判断是否是数字。
"""

m = input()
a = b = c = 0
for str in m:
    if str.isupper() :
        a = a + 1
    elif str.islower() :
        b = b + 1
    elif str.isdigit() :
        c = c + 1
print(a)
print(b)
print(c)
