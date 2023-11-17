'''
给出一个百分制成绩，要求输出成绩等级A、B、C、D、E。90分以上为A，80~89分为B，70~79分为C，60~69分为D，60分以下为E。
如果输入小于0或大于100的分数，则输出“Not valid”（注意大小写须一致）。
'''
# m = float(eval(input()))
# if 0 <= m < 60:
#     print('E')
# elif 60 <= m < 70:
#     print('D')
# elif 70 <= m < 80:
#     print('C')
# elif 80 <= m < 90:
#     print('B')
# elif 90 <= m < 100:
#     print('A')
# else:
#     print('Not valid')
'''
平均绩点计算方法：(课程学分1*绩点+课程学分2*绩点+课程学分n*绩点)/(课程学分1+课程学分2+课程学分n)
用户循环输入五分制成绩和课程学分，输入‘-1’时结束输入，计算学生平均绩点。等级与绩点对应关系如下表：
成绩       等级       绩点
90-100    A         4.0
85-89      A-        3.7
82-84      B+       3.3
78-81      B         3.0
75-77      B-        2.7
72-74      C+       2.3
68-71      C         2.0
64-67      C-        1.5
60-63      D         1.3
补考60     D-        1.0
60以下     F          0
'''

n,d,e=0,0,0

while True:
    m = input()

    if  m == '-1':
        break
    elif m == 'A':
        n = 4.0
    elif m == 'A-':
        n =3.7
    elif m == 'B+':
        n = 3.3
    elif m == 'B':
        n = 3.0
    elif m == 'B-':
        n = 2.7
    elif m == 'C+':
        n = 2.3
    elif m == 'C':
        n = 2.0
    elif m == 'C-':
        n =1.5
    elif m == 'D':
        n = 1.3
    elif m == 'D-':
        n = 1.0
    elif m == 'F':
        n = 0
    else:
        print()
        break
    q = float(eval(input()))#学分
    c = q * n
    d += c
    e += q
f = d/e
print('%.2f'%f)


