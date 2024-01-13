import numpy as np
a=eval(input())
arr=np.zeros((a,a))
for i in range(a):
    arr[i,i]=i+1
print(arr)