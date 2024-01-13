
def isprime(n):  #判断素数函数
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def f(n):        #找小于n的素数并求和
    ls = []
    a = 0
    for i in range(2,n+1):
        if isprime(i) :
            ls.append(i)
    ls =sorted(ls)[-10:]
    return sum(ls)
p=int(input())

print(f(p))
# # ##寻找素数要从2开始，因为0，1，n,三者都各自不满足客观条件