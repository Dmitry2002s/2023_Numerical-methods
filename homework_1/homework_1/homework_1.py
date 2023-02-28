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

print("Процедура отделения корней")
print("Отрезок, на котором выполняется отделение [-15,-10]")
A = -15
B = -10

N = 10 #Количество отрезков, котоыре проверяем на наличие корня нечётной кратности 
counter = 0 #Количество корней нечетной кратности 
List = [] 
H = (B-A)/N 
X1 = A 
X2 = X1 + H 
Y1 = f(X1) 
while (X2 <= B):##Находим, где меняется знак и считаем число корней
    Y2 = f(X2)
    if(Y1 * Y2 < 0):
        counter+=1 
        print("В интервале : [",X1,X2 , "] меняется знак ")
        interv = interval(X1,X2) 
        List.append(interv)
    X1=X2
    X2=X1+H 
    Y1 = Y2 
E = 0.000000000000001 #Допустимая ошибка для всех методов 
print("Эпсилон для всех методов равняется - " , E )
print("Число корней нечетной кратности - ", counter, "\n")
print("_____________________________________________________________________________") 
print("Метод бисекции")
time1 = time.perf_counter()
for i in List:
    A = i.X1 #Левая граница 
    B = i.X2 # Правая граница 
    
    S= 0 #количество шагов 
    while((B-A)>2*E):
        S+=1 
        C = (A+B)/2
        if(f(A)*f(C)<=0): 
            B = C 
        else: 
            A = C
    X = (A+B)/2
    D = (B-A)/2 
    print("Количество шагов - " , S )
    print("Приближенный корень  -" , X)
    print("Длина последнего отрезка -" , D)
    print("Абсолютная величина невязки -", f(X) , "\n") #Вычисление методом бисекции 
time2 = time.perf_counter() 
print("Время метода - ", time2-time1)
print("_____________________________________________________________________________") 
print("\nМетод Ньютона")

Z = 5*sympy.sin(2*y)-sqrt(1-y)
zprime =  Z.diff(y) 
zprime2 =  zprime.diff(y)
def Z(x): #значение функции в точке x 
    return 5*sympy.sin(2*x)-sqrt(1-x)
def Zprime(x): #Производная в точке x 
    return (zprime.evalf(subs = {y:x}))
def Zprime2(x): #2 Производная в точке x 
    return (zprime2.evalf(subs = {y:x}))
time1 = time.perf_counter()
for i in List: 
    A = i.X1 #Левая граница 
    B = i.X2 # Правая граница 
    
    S= 0 #количество шагов 
    #x_0 = A 
    #M = 0 
    #while(Z(x_0)*Zprime2(x_0)<0):
    #    x_0 = x_0 + (B-A)/100 
    #    M+=1 
    #    if (M == 100):
    #        x_0 = A + (B-A)/2 
    #        break #Поиск X_0 , уд-ее условиям теоремы 
    #b = x_0 
    while (abs( B - A ) > 2 * E):
        
       #if(Zprime(A)*Zprime(B)>0):
            #print("Есть перемена знаков произведения f' в точках x1 и x0, метод неприменим ")
            #break 
       # if (Zprime(A) == 0):
            #print("Производная в точке ", A, "равняется нулю")
        A = B 
        S+=1 
        B = A-f(A)/Zprime(A)
        if(S%100 ==0):
            print(S) 
    print("Количество шагов - " , S )
    print("Приближенный корень  -" , B)
    print("Длина последнего отрезка -" , B-A)
    print("Абсолютная величина невязки -", f(B) , "\n") #Метод Ньютона вычисления 
time2 = time.perf_counter() 
print("Время метода - ", time2-time1)
print("_____________________________________________________________________________") 
print("\n Усовершенствованный Метод Ньютона")
time1 = time.perf_counter()
for i in List: 
    A = i.X1 #Левая граница 
    B = i.X2 # Правая граница 
    
    S= 0 #количество шагов 
    x_0= A #т.к. всё задано в отрицательном, то просто возьмём середину отрезка 
    M = 0 
    
    while(Z(x_0)*Zprime2(x_0)<0):
        x_0 = x_0 + (B-A)/100 
        M+=1 
        if (M == 100):
            x_0 = A + (B-A)/2 
            break #Поиск X_0 , уд-ее условиям теоремы 

    while (abs( B - A ) > 2 * E):
        
       #if(Zprime(A)*Zprime(B)>0):
            #print("Есть перемена знаков произведения f' в точках x1 и x0, метод неприменим ")
            #break 
       # if (Zprime(A) == 0):
            #print("Производная в точке ", A, "равняется нулю")
        A = B 
        S+=1 
        B = A-f(A)/Zprime(x_0)
    print("Количество шагов - " , S )
    print("Приближенный корень  -" , B)
    print("Длина последнего отрезка -" , B-A)
    print("Абсолютная величина невязки -", f(B) , "\n") #Усовершенствованный Метод Ньютона вычисления 
time2 = time.perf_counter() 
print("Время метода - ", time2-time1)
print("_____________________________________________________________________________") 
print("\n Метод секущих ")
time1 = time.perf_counter()
for i in List: 
    A = i.X1 #Левая граница 
    B = i.X2 # Правая граница 
    C = 0 #Вычисляемое третье слагаемое 
    S= 0 #количество шагов 
    x_0= B + (A-B)/2  #т.к. всё задано в отрицательном, то просто возьмём середину отрезка
    while (abs( B - A ) > 2 * E):
       #if(Zprime(A)*Zprime(B)>0):
            #print("Есть перемена знаков произведения f' в точках x1 и x0, метод неприменим ")
            #break 
       # if (Zprime(A) == 0):
            #print("Производная в точке ", A, "равняется нулю")
        S+=1 
        C = B-(B-A)*f(B)/(f(B) - f(A))
        A = B 
        B = C 
    print("Количество шагов - " , S )
    print("Приближенный корень  -" , C)
    print("Длина последнего отрезка -" , B-A)
    print("Абсолютная величина невязки -", f(C) , "\n") #Метод секущих 
time2 = time.perf_counter() 
print("Время метода - ", time2-time1)
