import numpy as np
def main():

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    n, m = input().split()

    n = int(n)

    m = int(m)

    a = np.array(a)
    return n,m,a
if __name__=='__main__':
    n,m,a=main()
    b=0
    if n*m==12:
        arr=np.zeros((n,m))
        for i in range(n):
            for j in range(m):
                arr[i,j]=b+1
                b+=1
        print('{:}'.format(arr).replace('.',''))
    else:
        print("NO")