# -*- coding: cp1251 -*-

import sympy

from sympy.abc import x 

f = sympy.exp(6*x) 
def F(f, X): #Значение функции f в точке X 
    return f.evalf(subs = {x : X })
def F_1(f,X): #Возврашает производную в точке по формуле численного дифференцирования 
    if(X==0):
        return ((-3*f[X].value+4*f[X+1].value-f[X+2].value))/2/h
    elif(X == m - 1 ): 
        return ((3*f[X].value-4*f[X-1].value+f[X-2].value))/2/h
    return ((f[X+1].value-f[X-1].value)/(2*h))
def F_2(f,X):
   return (f[X+1].value - 2*f[X].value+ f[X-1].value)/(h**2)#Возвращает вторую производную 
#def numeral_diff(f):
#    return (f(a+h)-f(a-h))/2*h 
class cell (object):
    def __init__(self, number , value, diff1 = None, real_diff1 = None, diff2 = None, real_diff2 = None):
        self.number = number
        self.value = value
        self.diff1 = diff1 
        self.diff2 = diff2 
        self.real_diff1 = real_diff1 
        self.real_diff2 = real_diff2 

    def print(self):
        if(self.diff1 == None ):
            print(f"{self.number : < 25} {self.value : < 25} ")
        elif(self.diff2 == None ):
            print(f"{self.number : < 25} { self.value : < 25}{self.diff1 : ^25}{abs(self.real_diff1 - self.diff1) : ^25} ")
        else : 
            print(f"{self.number : <25}{self.value : ^25}{self.diff1 : ^25}{abs(self.real_diff1 - self.diff1) : ^25}{self.diff2 : ^25}{abs(self.real_diff2 - self.diff2)}") #Структура, которая хранит точку и значение в точке
List = []


#{self.value : <25}{self.diff1: <25}{self.diff2: <25}{self.real_diff1: <25}

a = 0 # float(input("Точка, где вычисляется производная\n"))
m =  10 #int(input("Число отрезков(число значений в таблице будет +1)\n"))
h = 0.1# float(input("Шаг таблицы ")) 
#/*for i in range(0,m):
#    if i == 0 or i == m - 1 :
#        List.append(cell(a+i*h,F(f,a+i*h),F_1_edge(List,i),diff2 = None,real_diff1 = f.diff(x).evalf(subs ={x : a+i*h}),real_diff2 = None))
#    elif i == 1 or i == m - 2  : 
#       List.append(cell(a+i*h,F(f,a+i*h),F_1(List,i),diff2 = F_2(List,i),real_diff1 = f.diff(x).evalf(subs ={x : a+i*h}),real_diff2 = f.diff(x).diff(x).evalf(subs ={x : a+i*h})))
#    else: 
#       List.append(cell(a+i*h,F(f,a+i*h),F_1(List,i),diff2 = F_2(List,i),real_diff1 = f.diff(x).evalf(subs ={x : a+i*h}),real_diff2 = f.diff(x).diff(x).evalf(subs ={x : a+i*h})))    



for i in range(0,m): 
    List.append(cell((a+i*h),F(f,a+i*h)))
for i in range(0,m): 
    List[i].diff1 = F_1(List,i) 
    List[i].real_diff1 = f.diff(x).evalf(subs ={x : a+i*h})
for i in range(1, m-1): 
    List[i].diff2 = F_2(List,i) 
    List[i].real_diff2 = f.diff(x).diff(x).evalf(subs ={x : a+i*h})
for i in List: 
    i.print() 
    print("Относительная величина невязки f' = ", (i.real_diff1 - i.diff1)/i.real_diff1)
    if(i.real_diff2 != None ):
        print("Относительная величина невязки f'' = ", (i.real_diff2 - i.diff2)/i.real_diff2)
    print("\n ")

