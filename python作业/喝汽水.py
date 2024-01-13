

def heqishui(n):
    c =0
    while n >= 2:
        a= int (n // 3)
        b = n % 3
        c += a
        n = a + b
        if n == 2:
            c = c + 1
            break
    return c
n = int(eval(input()))
print(heqishui(n))





