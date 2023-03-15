# -*- coding: cp1251 -*-
from cmath import inf
import math 
from math import exp
from types import ModuleType
import sympy 
from sympy import diff
from sympy.abc import x 

class cell (object):
    def __init__(self, number , value ):
        self.number = number
        self.value= value
    def print(self):
        print(f"{self.number : <25}{self.value : >25}") #���������, ������� ������ ����� � �������� � ����� 
class interval(object):
    def __init__(self, X1,X2):
        self.X1 = X1
        self.X2 = X2
    def print(self): 
        print("[ ",self.X1,",",self.X2, " ]") #���������, �������� �������� (� ����� ������ - ��� �������� ����(���� ������ �������� ���������))

def function(x):
    return 1 - math.exp(x) + x**2  #1 - math.exp(-x) + x**2 #���������� �������� ������� 

f = 1 - sympy.exp(-x) + x**2  

Table = list();  #������� �� ���������� ������� 

a = -10 # float(input("������� ����� ������� \n")) 
b = 10 # float(input("������� ������ ������� \n"))
m = 101 # int(input("���������� �������� ������� � �������\n"))

p = a 
for i in range(0,m):
    Table.append( cell( p + (b - a )*i / (m-1), function( p  + (b - a  ) * i / (m-1))) ) #��������� ������� ��������������� ���������� 
for i in Table: 
        i.print() #���������� ���� �������� 

#����� ������� ������� ������������ ������� : 

f_diff = f.diff(x)  #��������� ����������� ������� 

print(f_diff)
f_diff2 = f_diff.diff(x)

counter = 0 #����� ������ �������� ��������� 
N = 10000 #����� �������
List = [] #����, ���������� �������, ��� ����������� ������ ���� 
H = (b-a)/N
X1 = a 
X2 = X1 + H 
Y1 = f_diff.evalf(subs = {x:X1}) 
while (X2 <= b):##�������, ��� �������� ���� � ������� ����� ������
    Y2 = f_diff.evalf(subs = {x:X2})
    if(Y1 * Y2 < 0):
        counter+=1 
        print("� ��������� : [",X1,X2 , "] �������� ���� ����������� ")
        interv = interval(X1,X2) 
        List.append(interv)
    X1=X2
    X2=X1+H 
    Y1 = Y2 
monotony = [] 
if (len(List) == 0):
    print("������� ������ ��������� �� ��� [",a,",",b,"]")  
    monotony.append(interval(a,b)) 
else: 
    E = 0.000001 #�������-������
    for i in List: 
        A = i.X1 #����� ������� 
        B = i.X2 # ������ ������� 
        C = 0 #����������� ������ ��������� 
        x_0= B + (A-B)/2  #�.�. �� ������ � �������������, �� ������ ������ �������� �������
        while (abs( B - A ) > 2 * E):
            C = B-(B-A)*f_diff.evalf(subs ={x:B})/(f_diff.evalf(subs ={x:B}) - f_diff.evalf(subs ={x:A}))
            A = B 
            B = C 
        print("������������ ����� ��������� ����� �����������", C)
        if(len(monotony)==0):
            monotony.append(interval(a,C))
        else: 
            monotony.append(interval(len(monotony)-1, C))
        print("���������� �������� ������� -", f_diff.evalf(subs ={x:C}) , "\n") #����� ������� a
    monotony.append(interval(C,b)) 
for i in monotony:
    i.print() 

 
for m in monotony: 
    INTER = [] #������ �� ��������, �� ������� �������������. 
    for i in Table:
        if m.X1  < i.number < m.X2:
            INTER.append(cell(i.value,i.number))
    print("____________________________________________\n�������, �� ������� ������������� ")
    for i in INTER: 
        i.print() 
#####################################################################
choise = 1
while (choise == 1) :
    print("??????? ????? ????????????????") 
    x = float(input()) 

    print("??????? ???????? ??????? ????????????????? ??????????") 
    n = int(input("�� ������ �������� INTER")) 
    while (n>=len(INTER)):
        print("????????? ??????? ????????? ??? ????? ????? ???????? ??????? ? ???????\n????????? ???? ??????? ????????????????? ?????????? ")
        n = int(input()) 

    def nearest(x, List = Table):
        MIN = 2147483647
        l = 0 ##??????????????? ?????, ??????? ????????? ?? ???????
        Z = 0 ##?????? ????? ? ????? ???????? ???????? ???????? ? x 
        for i in List : 
            if(abs(i.number-x)<MIN):
                MIN = abs(i.number-x)
                Z = l 
            l+=1
        return Z 
    Z = nearest(x) #?????? ????????? ? ????? ???????????? ???? 
    print("????????? ???? = ", )
    Table[Z].print() 

    ITable = [] 
    ITable.append(Table[Z]) 
    c = n + 1  #?????????? ??? ????????? ?????, ??????? ? ????????? ?????? ????? ??????? ?????????? 
    p = 1
    while (c>1): #???????? ??????? ????????? ????? ???????????? ?? ???? ???????? 
        if(Z+p<m):
            ITable.append(Table[Z+p]) 
            c -= 1 
        if(Z-p>=0):
            ITable.append(Table[Z-p])
            c -= 1 
        if(c == 1):
            if(x-Table[Z].number > 0 ):
                if(Z+p+1<m):
                    ITable.append(Table[Z+p+1])
            else:
                if(Z-p-1>=m):
                    ITable.append(Table[Z-p-1])
            break
        p+=1 
    print("??????????????? ?? ??????????? ?????????? ?? ???? ???????????? ??????? ?????, ?? ??????? ????????? ????????????????")
    for i in ITable :
        i.print() 

    #???????????????? ? ????? ????????? 

    result_L = 0     
    for k in range (0, n) :
        w = 1 # ????????? ? ???????????????? ??????? ????????? 
        w_= 1 # ??????????? 
        for i in range (0,n) :
            if(k!=i): 
                w *= (x-ITable[i].number) 
                w_*= ITable[k].number-ITable[i].number
       
        result_L += (w/w_) *ITable[k].value


    print("???????? ????????????????? ?????????? ? ????? ????????? ? ????? ",x, " = " , result_L) 
    print("??????? ????????????????? ?????????? ? ???????  = ", abs(result_L - function(x)), "\n")

    result_N = 0 

    q = 1 
    ITable_N = []
    for i in range(0,n) :
        ITable_N.append(ITable[i])
        result_N+=f(ITable_N)*q 
        q*=(x-ITable_N[i].number)

    print("\n????????? ????????????????? ?????????? ? ????? ??????? ", result_N)
    print("??????? ????????????????? ?????????? ? ???????  = ", abs(result_N - function(x)), "\n""\n""\n""\n")
    print("?????? ?????????????????? ?????? ????? ? \n 0 - ???, 1 - ??")
    choise = -1 
    while(choise != 0 and choise != 1) :
        choise = int(input())
        if (choise != 0 and choise != 1):
            print("???????????, ??????? ????????") 
        if (choise == 0):
            break
