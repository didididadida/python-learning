import numpy as np
a,b=eval(input().replace(' ',','))
arr=np.zeros(a)
arr[b-1]=1
print('[{:}]'.format(arr))