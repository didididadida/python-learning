import os
t = 5
s = 'hello world!'
with open('test.txt', 'a+') as file0:
    # w：覆盖重写    a: 接着续写
    print('%d' % t,'%s' % s,file=file0)
