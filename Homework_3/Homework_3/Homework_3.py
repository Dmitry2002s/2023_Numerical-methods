# -*- coding: cp1251 -*-

from cmath import inf
import math 
from math import exp
from types import ModuleType
import sympy 
from sympy import diff
from sympy.abc import x,v 

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
    return 1 - math.exp(-x) + x**2  #1 - math.exp(-x) + x**2 #���������� �������� ������� 
f = 1 - sympy.exp(-x) + x**2 

Table = list();  #������� �� ���������� ������� 

a = -7 # float(input("������� ����� ������� \n")) 
b = 10 # float(input("������� ������ ������� \n"))
m = 101 # int(input("���������� �������� ������� � �������\n"))

p = a 
for i in range(0,m):
    Table.append( cell( p + (b - a )*i / (m-1), function( p  + (b - a  ) * i / (m-1))) ) #��������� ������� ��������������� ���������� 
for i in Table: 
        i.print() #���������� ���� �������� 

#����� ������� ������� ������������ ������� : 

f_diff = f.diff(x)  #��������� ����������� ������� 

#print(f_diff)
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
        #print("� ��������� : [",X1,X2 , "] �������� ���� ����������� ")
        interv = interval(X1,X2) 
        List.append(interv)
    X1=X2
    X2=X1+H 
    Y1 = Y2 
monotony = [] 
E = 0.0000001#������� ������ ��� ������ �������� �������������� 
if (len(List) == 0):
    #print("������� ������ ��������� �� ��� [",a,",",b,"]")  
    monotony.append(interval(a,b)) 
else: 
     #�������-������
    for i in List: 
        A = i.X1 #����� ������� 
        B = i.X2 # ������ ������� 
        C = 0 #����������� ������ ��������� 
        x_0= B + (A-B)/2  #�.�. �� ������ � �������������, �� ������ ������ �������� �������
        while (abs( B - A ) > 2 * E):
            C = B-(B-A)*f_diff.evalf(subs ={x:B})/(f_diff.evalf(subs ={x:B}) - f_diff.evalf(subs ={x:A}))
            A = B 
            B = C 
        #print("������������ ����� ��������� ����� �����������", C)
        if(len(monotony)==0):
            monotony.append(interval(a,C))
        else: 
            monotony.append(interval(len(monotony)-1, C))
       # print("���������� �������� ������� -", f_diff.evalf(subs ={x:C}) , "\n") #����� ������� a
    monotony.append(interval(C,b)) 
#print("���������� ������������ : ")
for i in monotony:
    i.print() 
choise = 1
while (choise == 1) :
    E = float(input("������� �-������ ��� ��������\n")) #()) 
    print("������� ����� ����������������, ��������������� �������� ������� ������ ������ ") 
    x = float(input())
    print("������� �������� ������� ����������������� ����������") 
    n = int(input()) 
        
    for m in monotony: 
        INTER = [] #������ �� ��������, �� ������� �������������. 
        for i in Table:
            if m.X1  < i.number < m.X2:
                INTER.append(cell(i.value,i.number))
        #print("____________________________________________\n�������, �� ������� ������������� ")
        while (n>=len(INTER)):
                print("��������� ������� ��������� ��� ����� ����� �������� ������� � �������\n��������� ���� ������� ����������������� ���������� ")
                n = int(input())
        #for i in INTER: 
        #    i.print() 
            
        
    
        def nearest(x, List = INTER):
                MIN = 2147483647
                l = 0 ##��������������� �����, ������� ��������� �� �������
                Z = 0 ##������ ����� � ����� �������� �������� �������� � x 
                for i in List : 
                    if(abs(i.number-x)<MIN):
                        MIN = abs(i.number-x)
                        Z = l 
                    l+=1
                return Z 

        Z = nearest(x) #������ ��������� � ����� ������������ ���� 
        #print("��������� ���� = ",Z )

        ITable = [] 
        ITable.append(INTER[Z]) 
        c = n + 1  #���������� ��� ��������� �����, ������� � ��������� ������ ����� ������� ���������� 
        p = 1
        m = len(INTER)
        while (c>1): #�������� ������� ��������� ����� ������������ �� ���� �������� 
            if(Z+p<m):
                ITable.append(INTER[Z+p]) 
                c -= 1 
            if(Z-p>=0):
                ITable.append(INTER[Z-p])
                c -= 1 
            if(c == 1):
                if(x-Table[Z].number > 0 ):
                    if(Z+p+1<m):
                        ITable.append(INTER[Z+p+1])
                else:
                    if(Z-p-1>=m):
                        ITable.append(INTER[Z-p-1])
                break
            p+=1 
        #print("��������������� �� ����������� ���������� �� ���� ������������ ������� �����, �� ������� ��������� ����������������")
        #for i in ITable :
        #    i.print() 

        #���������������� � ����� ��������� 
        result_L1 = 0   
        
        for k in range (0, n) :
            w = 1 # ��������� � ���������������� ������� ��������� 
            w_= 1 # ����������� 
            for i in range (0,n) :
                if(k!=i): 
                    w *= (x-ITable[i].number) 
                    w_*= ITable[k].number-ITable[i].number
       
            result_L1 += (w/w_) *ITable[k].value

        print("�������� ����������������� ���������� � ����� ��������� � ����� ",x, " = " , result_L1) 
        print("������� ����������������� ���������� � �������  = ", abs(function(result_L1)-x), "\n")
    
    


    print("_______________________________\n2�� ����� ������� ������")
    result_L = 0 
    ITable = []
    
        #print("��������� ���� = ",Z )
    V = 0 #����� ���������� ������������ 
    P_i = 0 #����� ������������� �������� � ���������� ������������ 
    Z = nearest(x, Table) #������ ��������� � ����� ������������ ���� 
    for i in monotony:
        if (Z > i.X1 and Z<i.X2):
            break
        p+=1 
    
        
    ITable = [] 
    ITable.append(Table[Z]) 
    c = n + 1  #���������� ��� ��������� �����, ������� � ��������� ������ ����� ������� ���������� 
    p = 1
    m = len(Table)
    VAX = len(ITable)#���� ��������� ���������� ������� 
    CAX = 0 
    AAAP = 0 

    while (c>1): #�������� ������� ��������� ����� ������������ �� ���� �������� 
            if(Z+p<m and c!= 1):
                if(Table[Z+p].number>monotony[V].X1 and Table[Z+V].number<monotony[V].X2 ):
                    ITable.append(Table[Z+p]) 
                    c -= 1 
            if(Z-p>=0 and c!= 1 ):
                if(Table[Z-p].number>monotony[V].X1 and Table[Z-p].number<monotony[V].X2 ):
                    ITable.append(Table[Z-p])
                    c -= 1 
            if(c == 1):
                if(x-Table[Z].number > 0 ):
                    if(Z+p+1<m):
                        if(Table[Z+p+1].number>monotony[V].X1 and Table[Z+p+1].number<monotony[V].X2 ):
                            ITable.append(Table[Z+p+1])
                             
                else:
                    if(Z-p-1>=m):
                        if(Table[Z+p-1].number>monotony[V].X1 and Table[Z+p-1].number<monotony[V].X2 ):
                            ITable.append(Table[Z-p-1])

                break
            p+=1
            
            #if(len(ITable) == VAX):
            #    VAX = len(ITable) 
            #    CAX += 1 
            #    if CAX == 2: 
            #        AAAP = 1 
            #        break 
            #else:
            #    CAX = 0 
            #if(AAAP==0):
            #    break 


    #print("��������������� �� ����������� ���������� �� ���� ������������ ������� �����, �� ������� ��������� ����������������")
    #for i in ITable :
    #    i.print() 
    n = len(ITable) 
    for k in range (0, n) :
            w = 1 # ��������� � ���������������� ������� ��������� 
            w_= 1 # ����������� 
            for i in range (0,n) :
                if(k!=i): 
                    w *= (v-ITable[i].number) 
                    w_*= ITable[k].number-ITable[i].number
       
            result_L += (w/w_) *ITable[k].value
    CVA = result_L - x #�������� ��������� ��� 2��� ������ 
    AAAAA = []
        
    A = a
    B = b
    N = 1000 #���������� ��������, ������� ��������� �� ������� ����� �������� ��������� 
    counter = 0 #���������� ������ �������� ��������� 
    List = [] 
    H = (B-A)/N 
    X1 = A 
    X2 = X1 + H 
    Y1 = CVA.evalf(subs = {v:X1}) 
    while (X2 <= B):##�������, ��� �������� ���� � ������� ����� ������
        Y2 = CVA.evalf(subs = {v:X2})
        if(Y1 * Y2 < 0):
            counter+=1 
            print("� ��������� : [",X1,X2 , "] �������� ���� ")
            interv = interval(X1,X2) 
            AAAAA.append(interv)
        X1=X2
        X2=X1+H 
        Y1 = Y2 
    for i in AAAAA:
        A = i.X1 #����� ������� 
        B = i.X2 # ������ ������� 
        C = 0 #����������� ������ ��������� 
        x_0= B + (A-B)/2  #�.�. �� ������ � �������������, �� ������ ������ �������� �������
        kk = 0 
        while (abs( B - A ) > 2 * E or kk == 0 ):
            C = B-(B-A)*CVA.evalf(subs = {v:B})/(CVA.evalf(subs = {v:B}) - CVA.evalf(subs = {v:A}))
            A = B 
            B = C 
            kk = 1 
        print("������������ ������  -" , C)
        print("���������� �������� ������� -", abs(function(C) - x) , "\n") #����� �������
    print("������ ������������������ ������ ����� ? \n 0 - ���, 1 - ��")
    choise = -1 
    while(choise != 0 and choise != 1) :
        choise = int(input())
        if (choise != 0 and choise != 1):
            print("�����������, ������� ��������") 
        if (choise == 0):
            break
