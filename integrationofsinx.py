from math import *
def integration(x1,x2):
    n=int(input("how many iterations: "))
    h=(x2-x1)/n
    sum=0
    for i in range(n):
        sum=sum+h*sin(x1+i*h)
    print("the integral value= ", sum)
    return sum
x1=float(input("lower limit= "))
x2=float(input("upper limit= "))
integration(x1,x2)