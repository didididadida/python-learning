count=1
def hanoi(n,a,b,c):
    global count
    if n==1:
        if count>=10:
            print("[STEP  {}] {}->{}".format(count,a, c))
        else:
            print("[STEP   {}] {}->{}".format(count,a, c))
        count+=1
    else:
        hanoi(n-1,a,c,b)
        if count>=10:
            print("[STEP  {}] {}->{}".format(count, a,c))
        else:
            print("[STEP   {}] {}->{}".format(count, a,c))
        count+=1
        hanoi(n-1,b,a,c)
n=eval(input())
hanoi(n, 'A', 'B', 'C')
