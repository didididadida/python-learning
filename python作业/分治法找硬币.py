def jia(n):
    a=0
    for i in n:
        a+=eval(i)
    return a
def findFalseCoin(coins,s,n):
    if n==2:
        if coins[0]!=coins[1]:
            if eval(coins[0]) < eval(coins[1]):
                print("Fake coin:{:}".format(s))
            else:
                print("Fake coin:{:}".format(s + 1))
        else:
            print("Fake coin is not found")
    elif n%2 ==0:
        if jia(coins[s:s+n//2])<jia(coins[s+n//2:s+n]):
            findFalseCoin(coins[s:s+n//2],s,n//2)
        elif jia(coins[s:s+n//2])>jia(coins[s+n//2:s+n]):
            findFalseCoin(coins[s+n//2:s+n],s+n//2,n//2)
        else:
            print("Fake coin is not found")
    else:
        if jia(coins[s:s+(n-1)//2])<jia(coins[s+(n-1)//2:s+n-1]):
            findFalseCoin(coins[s:s+(n-1)//2],s,(n-1)//2)
        elif jia(coins[s:s+(n-1)//2])>jia(coins[s+(n-1)//2:s+n-1]):
            findFalseCoin(coins[s+(n-1)//2:s+n-1],s+(n-1)//2,(n-1)//2)
        else:
            print("Fake coin:{:}".format(s+n-1))
a=input().split(',')
findFalseCoin(a,0,len(a))