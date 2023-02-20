
 
import math
from typing import Counter
def f(x):
    return (5*math.sin(2*x)-math.sqrt(1-x))

print("Enter number in range from -15 to -10")
x = int(input()) 


if (x >-15 and x<-10):
    print("function in point ", x, " = ", f(x) )
else: 
    print("Incorrect argument")
    
print("Enter the left border")
A = int(input())
print("Enter the right border")
B = int(input())
if ( B < A ):
    C = A
    A = B 
    B = A 
    print("Enter borders is incorrect, borders swapped ")



N = 10 
counter = 0 
H = (B-A)/N 
X1 = A 
X2 = X1 + H 
Y1 = f(X1) 
while (X2 <= B):
    Y2 = f(X2)
    if(Y1 * Y2 < 0):
        counter+=1 
        print("In this interval : [",X1,X2 , "] the sign changes")
    X1=X2
    X2=X1+H 
    Y1 = Y2 
print("The number of roots : ", counter)

print("root search by half division method")

print("Enter the left border")
A = float(input())
print("Enter the right border")
B = float(input())
if ( B < A ):
    C = A
    A = B 
    B = A 
    print("Enter borders is incorrect, borders swapped ")

print("Enter epsilon")
E = float(input())

while((B-A)>2*E):
    C = (A+B)/2
    if(f(A)*f(C)<=0): 
        B = C 
    else: 
        A = C
X = (A+B)/2
D = (B-A)/2 
print("approximate root :" , X)
print("Error rate :" , D)
print("Function value", f(X) )