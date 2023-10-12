
'''
用异常处理改进温度转换程序，使其能够接收并处理用户的异常输入。
'''
def tempconvert(valuestr):
    if valuestr[-1] in ['F','f']:
        C = (eval(valuestr[0:-1])-32)/1.8
        print('The converted temperature is {}C'.format(int(C)))
    elif valuestr[-1] in ['C','c']:
        F = eval(valuestr[0:-1]) * 1.8 + 32
        print('The converted temperature is {}F'.format(int(F)))
    else:
        print("End with 'C','c','F','f'")

try:
    tempstr = input("What is the temperature?")
    tempconvert(tempstr)
except:
    print('Input error')