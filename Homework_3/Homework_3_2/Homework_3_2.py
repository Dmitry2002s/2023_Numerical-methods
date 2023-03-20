# -*- coding: cp1251 -*-

import sympy

from sympy.abc import x 

f = sympy.exp(6*x) 
def F(f, X): #Значение функции f в точке X 
    return f.evalf(subs = {x : X })
def F_1(f,X): #Возврашает производную в точке по формуле численного дифференцирования 
   
    return ((F(f,X+h)-F(f,X-h))/(2*h))
def F_2(f,X):
   return ((F_1(f,X+h)-F_1(f,X-h))/(2*h))#Возвращает вторую производную 
def numeral_diff(f):
    return (f(a+h)-f(a-h))/2*h 
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
            print(f"{self.number : < 20} {self.value : < 20} ")
        elif(self.diff2 == None ):
            print(f"{self.number : < 20} { self.value : < 20}{self.diff1 : ^20}{abs(self.real_diff1 - self.diff1) : ^20} ")
        else : 
            print(f"{self.number : <20}{self.value : ^20}{self.diff1 : ^20}{abs(self.real_diff1 - self.diff1) : ^20}{self.diff2 : ^20}{abs(self.real_diff2 - self.diff2)}") #Структура, которая хранит точку и значение в точке
List = []


#{self.value : <20}{self.diff1: <20}{self.diff2: <20}{self.real_diff1: <20}

a = -2 # float(input("Точка, где вычисляется производная\n"))
m =  100 #int(input("Число отрезков(число значений в таблице будет +1)\n"))
h = 0.1# float(input("Шаг таблицы ")) 
for i in range(0,m):
    if i == 0 or i == m :
        List.append(cell(a+i*h,F(f,a+i*h),None,None,None,None))
    elif i == 1 or i == m - 1 : 
       List.append(cell(a+i*h,F(f,a+i*h),F_1(f,a+i*h),diff2 = None,real_diff1 = f.diff(x).evalf(subs ={x : a+i*h}),real_diff2 = None))
    else: 
       List.append(cell(a+i*h,F(f,a+i*h),F_1(f,a+i*h),diff2 = F_2(f,a+i*h),real_diff1 = f.diff(x).evalf(subs ={x : a+i*h}),real_diff2 = f.diff(x).diff(x).evalf(subs ={x : a+i*h})))    
for i in List: 
    i.print() 

