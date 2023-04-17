# -*- coding: cp1251 -*-

import sympy
from sympy import sin, cos ,exp, integrate,sympify
from sympy.abc import x
def function(f,y):# �������� ������� � ����� x:
    return f.evalf(subs = {x : y})
def integrate_KF(list_f): 
    for f in list_f :  
            F = integrate(f,x) 
            print("_______________________________________")
            print("������ �������� ��������� ��� ������� \n    ",f," \n�� ���������� [",a,",",b,"]    =   ", function(F,b) - function(F,a))  
            print("��������������� �������� ��������� ��� ������ ..... ���������� ����������� ���������� \n")
            print("�� ������ �������������� = ", (b-a)*function(f,a) , " -  ",abs((b-a)*function(f,a)-(function(F,b) - function(F,a))) )
            print("������� ��������������   = ", (b-a)*function(f,b), " -  ",abs((b-a)*function(f,b)-(function(F,b) - function(F,a))) )
            print("�������� ��������������  = ", (b-a)*function(f,(a+b)/2), " -  ",abs((b-a)*function(f,(a+b)/2)-(function(F,b) - function(F,a))))
            print("��������                 = ", (b-a)/2*(function(f,a) + function(f,b)), " -  ",abs((b-a)/2*(function(f,a) + function(f,b))-(function(F,b) - function(F,a))) ) 
            print("��������                 = ", (b-a)/6*(function(f,a) + function(f,b) +4*function(f,(a+b)/2)), " -   ",abs((b-a)/6*(function(f,a) + function(f,b) +4*function(f,(a+b)/2))-(function(F,b) - function(F,a))) )
            print("3/8                      = ", (b-a)/8*(function(f,a) + function(f,b) +3*function(f,a+(b-a)/3)+3*function(f,a+2*(b-a)/3)), " -  ",abs(-(function(F,b) - function(F,a))+ (b-a)/8*(function(f,a) + function(f,b) +3*function(f,a+(b-a)/3)+3*function(f,a+2*(b-a)/3))) )
            print("_______________________________________")
def SKF_Left_triangle(f,m, a ,b ):
    F = integrate(f,x) 
    h = (b - a) / m 
    result = 0 
    for j in range(0,m): 
        result += function(f,a+j*h)
    result *= h 
    print("C�� ������ ������������  = ", result , " -  ",abs(result-(function(F,b) - function(F,a))) )
    
    return result 
def SKF_Right_triangle(f,m, a ,b ): 
    F = integrate(f,x)
    h = (b - a) / m 
    result = 0 
    for j in range(0,m): 
        result += function(f,a+(j+1)*h)
    result *= h 
    print("C�� ������� ������������  = ", result , " -  ",abs(result-(function(F,b) - function(F,a))) )
     
    return result 
def SKF_Middle_triangle(f,m, a ,b ): 
    F = integrate(f,x)
    h = (b - a) / m 
    result = 0 
    for j in range(0,m): 
        result += function(f,a+(j+1/2)*h)
    result *= h 
    print("C�� �������� ������������ = ", result , " -  ",abs(result-(function(F,b) - function(F,a))) )
     
    return result 
def SKF_Trapezoid(f,m, a ,b ): 
    F = integrate(f,x)
    h = (b - a) / (m) 
    result = 0 
    for j in range(0,m): 
        result += (function(f,a+j*h) + function(f,a+(j+1)*h))/2
    result *= h
    print("C�� ��������              = ", result , " -  ",abs(result-(function(F,b) - function(F,a))) )
     
    return result 
def SKF_Simpson(f,m, a ,b ): 
    F = integrate(f,x)
    h = (b-a)/(m)
    result = 0
    for j in range(0,m): 
        result += function(f,a+j*h) + 4*function(f,a+(j+1/2)*h) + function(f,a+(j+1)*h)
    result *= h/6
    print("C�� ��������              = ", result , " -  ",abs(result-(function(F,b) - function(F,a))) )
            
    return result 
def integrate_SKF(list_f):
    m = int(input("������� ����� ����������� ������� "))
    list_SKF = [SKF_Left_triangle ,SKF_Right_triangle,SKF_Middle_triangle,SKF_Trapezoid,SKF_Simpson]
    for f in list_f :  
        F = integrate(f,x) 
        print("_______________________________________")
        print("������ �������� ��������� ��� ������� \n  ",f," \n�� ���������� [",a,",",b,"]    =   ", function(F,b) - function(F,a))
        print("_______________________________________") 
        for k in list_SKF: 

            k(f,m ,a,b) 
        

#a,b = input().split() 
#a,b = int(a), int(b)

a,b = 0,2  

list_f = [x**0, x**1 ,x**2, x**3, x**4, x**3+sin(x)]
i = 1
'''while(i != '0'):
    print("������� ������� ��� ��������������(�� x) , �� ��������� ������ ������� 0")
    i = input()
    if(i != '0') :
        list_f.append(sympify(i)) '''
choise = 0 
while(choise != '0') :
    i =  1 
    print("����  \n 1 - �� \n 2 - ��� \n 3 - ��������� ������ ������������� ������� ")
    print(" 4 - ���������� ������ ������������� ������� � ������� ��������������   \n 5 - �������� ������� �������������� \n 0 - ��������� ������ ����������")
    choise = int(input())
    if choise == 0 : 
        break 
    elif choise == 1 :  
        integrate_KF(list_f)
    elif choise == 2 : 
        integrate_SKF(list_f)
    elif choise == 3 : 
        while(i != '0'):
            print("������� ������� ��� ��������������(�� x) , �� ��������� ������ ������� 0")
            i = input()
            if(i != '0') :
                list_f.append(sympify(i)) 
    elif choise == 4 : 
        print(list_f) 
        print("[" , a ," , " ,b, "]")
    elif choise == 5 : 
        a = float(input("������� ����� ������\n"))
        b = float(input("������� ������ ������\n"))
        print("������, ������� ��������")


