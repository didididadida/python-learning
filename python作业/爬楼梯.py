def palouti(n):
    if n <= 3:
        return n
    else:
        return   palouti(n-1) + palouti(n-2)


n = eval(input()) -1
print(palouti(n))
