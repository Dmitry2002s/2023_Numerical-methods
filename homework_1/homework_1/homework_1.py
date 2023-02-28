# -*- coding: cp1251 -*-

import time 
import math
from typing import Counter
import sympy 
from sympy import diff, sin ,sqrt 
from sympy.abc import y,z 
def f(x):
    return (5*math.sin(2*x)-math.sqrt(1-x))
class interval(object):
    def __init__(self, X1,X2):
        self.X1 = X1
        self.X2 = X2
    def Print(self): 
        print("[ ",self.X1,",",self.X2, " ]")


time1 = 0 
time2 = 0 

print("��������� ��������� ������")
print("�������, �� ������� ����������� ��������� [-15,-10]")
A = -15
B = -10

N = 10 #���������� ��������, ������� ��������� �� ������� ����� �������� ��������� 
counter = 0 #���������� ������ �������� ��������� 
List = [] 
H = (B-A)/N 
X1 = A 
X2 = X1 + H 
Y1 = f(X1) 
while (X2 <= B):##�������, ��� �������� ���� � ������� ����� ������
    Y2 = f(X2)
    if(Y1 * Y2 < 0):
        counter+=1 
        print("� ��������� : [",X1,X2 , "] �������� ���� ")
        interv = interval(X1,X2) 
        List.append(interv)
    X1=X2
    X2=X1+H 
    Y1 = Y2 
E = 0.000000000000001 #���������� ������ ��� ���� ������� 
print("������� ��� ���� ������� ��������� - " , E )
print("����� ������ �������� ��������� - ", counter, "\n")
print("_____________________________________________________________________________") 
print("����� ��������")
time1 = time.perf_counter()
for i in List:
    A = i.X1 #����� ������� 
    B = i.X2 # ������ ������� 
    
    S= 0 #���������� ����� 
    while((B-A)>2*E):
        S+=1 
        C = (A+B)/2
        if(f(A)*f(C)<=0): 
            B = C 
        else: 
            A = C
    X = (A+B)/2
    D = (B-A)/2 
    print("���������� ����� - " , S )
    print("������������ ������  -" , X)
    print("����� ���������� ������� -" , D)
    print("���������� �������� ������� -", f(X) , "\n") #���������� ������� �������� 
time2 = time.perf_counter() 
print("����� ������ - ", time2-time1)
print("_____________________________________________________________________________") 
print("\n����� �������")

Z = 5*sympy.sin(2*y)-sqrt(1-y)
zprime =  Z.diff(y) 
zprime2 =  zprime.diff(y)
def Z(x): #�������� ������� � ����� x 
    return 5*sympy.sin(2*x)-sqrt(1-x)
def Zprime(x): #����������� � ����� x 
    return (zprime.evalf(subs = {y:x}))
def Zprime2(x): #2 ����������� � ����� x 
    return (zprime2.evalf(subs = {y:x}))
time1 = time.perf_counter()
for i in List: 
    A = i.X1 #����� ������� 
    B = i.X2 # ������ ������� 
    
    S= 0 #���������� ����� 
    #x_0 = A 
    #M = 0 
    #while(Z(x_0)*Zprime2(x_0)<0):
    #    x_0 = x_0 + (B-A)/100 
    #    M+=1 
    #    if (M == 100):
    #        x_0 = A + (B-A)/2 
    #        break #����� X_0 , ��-�� �������� ������� 
    #b = x_0 
    while (abs( B - A ) > 2 * E):
        
       #if(Zprime(A)*Zprime(B)>0):
            #print("���� �������� ������ ������������ f' � ������ x1 � x0, ����� ���������� ")
            #break 
       # if (Zprime(A) == 0):
            #print("����������� � ����� ", A, "��������� ����")
        A = B 
        S+=1 
        B = A-f(A)/Zprime(A)
        if(S%100 ==0):
            print(S) 
    print("���������� ����� - " , S )
    print("������������ ������  -" , B)
    print("����� ���������� ������� -" , B-A)
    print("���������� �������� ������� -", f(B) , "\n") #����� ������� ���������� 
time2 = time.perf_counter() 
print("����� ������ - ", time2-time1)
print("_____________________________________________________________________________") 
print("\n ������������������� ����� �������")
time1 = time.perf_counter()
for i in List: 
    A = i.X1 #����� ������� 
    B = i.X2 # ������ ������� 
    
    S= 0 #���������� ����� 
    x_0= A #�.�. �� ������ � �������������, �� ������ ������ �������� ������� 
    M = 0 
    
    while(Z(x_0)*Zprime2(x_0)<0):
        x_0 = x_0 + (B-A)/100 
        M+=1 
        if (M == 100):
            x_0 = A + (B-A)/2 
            break #����� X_0 , ��-�� �������� ������� 

    while (abs( B - A ) > 2 * E):
        
       #if(Zprime(A)*Zprime(B)>0):
            #print("���� �������� ������ ������������ f' � ������ x1 � x0, ����� ���������� ")
            #break 
       # if (Zprime(A) == 0):
            #print("����������� � ����� ", A, "��������� ����")
        A = B 
        S+=1 
        B = A-f(A)/Zprime(x_0)
    print("���������� ����� - " , S )
    print("������������ ������  -" , B)
    print("����� ���������� ������� -" , B-A)
    print("���������� �������� ������� -", f(B) , "\n") #������������������� ����� ������� ���������� 
time2 = time.perf_counter() 
print("����� ������ - ", time2-time1)
print("_____________________________________________________________________________") 
print("\n ����� ������� ")
time1 = time.perf_counter()
for i in List: 
    A = i.X1 #����� ������� 
    B = i.X2 # ������ ������� 
    C = 0 #����������� ������ ��������� 
    S= 0 #���������� ����� 
    x_0= B + (A-B)/2  #�.�. �� ������ � �������������, �� ������ ������ �������� �������
    while (abs( B - A ) > 2 * E):
       #if(Zprime(A)*Zprime(B)>0):
            #print("���� �������� ������ ������������ f' � ������ x1 � x0, ����� ���������� ")
            #break 
       # if (Zprime(A) == 0):
            #print("����������� � ����� ", A, "��������� ����")
        S+=1 
        C = B-(B-A)*f(B)/(f(B) - f(A))
        A = B 
        B = C 
    print("���������� ����� - " , S )
    print("������������ ������  -" , C)
    print("����� ���������� ������� -" , B-A)
    print("���������� �������� ������� -", f(C) , "\n") #����� ������� 
time2 = time.perf_counter() 
print("����� ������ - ", time2-time1)
