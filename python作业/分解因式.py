
n = eval(input())
ls = []
while n != 1:
    for i in range(2,n+1):
        while  n%i == 0:
            ls.append(i)
            n /= i
print(ls)

