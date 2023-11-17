'''
编写猜数游戏程序，功能是：允许用户反复输入数，直至猜中程序选定的数（假定为100）。
输入的数如果大于选定的数，则提示"larger than expected"；如果小于选定的数，则提示"less than expected"；
如果等于选定的数，则输出"you win"并结束程序。
'''

n = 100
N = 0
while True:
    N += 1
    try:
        m = eval(input())
        if m < n:
            print('less than expected')
        elif m > n:
            print("larger than expected")
        else:
            print("you have tried", N,"times, you win")
            break
    except:
        print("input error")
