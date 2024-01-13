import numpy as np
arr = input("")
a = [float(x) for x in arr.split()]
a.sort()
arr=np.array(a)
print(arr)
