'''
将两个整型数组按照升序合并，并且过滤掉重复数组元素

'''
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
c=set(a+b)
d=list(c)
e=sorted(d)
# print(" ".join(str(e)))
print("".join(str(q) for q in e))
#print(" ".join([str(q) for q in sorted((list(set(a+b))))]))

