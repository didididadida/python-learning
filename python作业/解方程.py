import math

a = int(input())
b = int(input())
c = int(input())
formula = b**2-4*a*c
x1 = (-b+math.sqrt(formula))/(2*a)
x2 = (-b-math.sqrt(formula))/(2*a)
if formula<0:
     print("出错了")
elif formula == 0:
        print(-b/(a*2))
else:
        print(f"{x1},{x2}")  #‘f’类似于format
