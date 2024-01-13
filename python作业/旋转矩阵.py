a=eval(input())
i=1
k=a
c,d,e=0,0,a**2
arr = [[0 for h in range(a)] for j in range(a)]
while i<=e:
    for n in range(a):
        arr[c][d]=i
        i+=1
        d+=1#c=0,d=4,right
    d-=1
    a-=1
    for k in range(a):
        c+=1#c=3,d=3,down
        arr[c][d]=i
        i+=1
    for s in range(a):
        d-=1
        arr[c][d]=i#c=3,d=0,left
        i+=1
    a-=1
    for g in range(a):
        c-=1
        arr[c][d]=i#c=1,d=0,up
        i+=1
    d+=1
with open('file.out','w') as f:
    for i in arr:
        for j in i:
           print("%5d"%j,file=f,end='')
        print('\n',file=f)
with open('file.out','r') as f:
    print(f.read())