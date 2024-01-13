import math
def prime(p):
    for i in range(2, int(math.sqrt(p)) + 1): #一
        if p % i == 0:
            return False
    return True
n = int(input())
if n  % 2 != 0:
    print("Data error!")
else:
    for i in range(2, int(n / 2) + 1):
        if prime(i) and prime(n - i):  #二
            print('N', "=", i, "+", n - i)
            break
