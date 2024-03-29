﻿
import sympy
from sympy import sin, cos ,exp, integrate,sympify
from sympy.abc import x
import math 
def function(f,y):# Значение функции в точке x:
    return f.evalf(subs = {x : y})

def MAX_f(f ,a,b): 
    h = 1/100
    i = 0
    result = -10000000
    while(a+i*h<b):
        if(function(f,(a+i*h))>result):
            result = function(f,a+i*h)
        i+=1 
    return result 
def f_diff(f,n):
    while(n!=0):
        f = f.diff(x)
        n-=1 
    return f 
def integrate_KF(list_f): 
    for f in list_f :  
            F = integrate(f,x) 
            print("_______________________________________")
            print("Точное значение интеграла для функции \n    ",f," \nНа промежутке [",a,",",b,"]    =   ", function(F,b) - function(F,a))  
            print("Приблизительное значение интеграла при помощи ..... Абсолютная погрешность составляет \n")
            print("КФ левого прямоугольника = ", (b-a)*function(f,a) , " -  ",abs((b-a)*function(f,a)-(function(F,b) - function(F,a))) )
            print("правого прямоугольника   = ", (b-a)*function(f,b), " -  ",abs((b-a)*function(f,b)-(function(F,b) - function(F,a))) )
            print("среднего прямоугольника  = ", (b-a)*function(f,(a+b)/2), " -  ",abs((b-a)*function(f,(a+b)/2)-(function(F,b) - function(F,a))))
            print("трапеции                 = ", (b-a)/2*(function(f,a) + function(f,b)), " -  ",abs((b-a)/2*(function(f,a) + function(f,b))-(function(F,b) - function(F,a))) ) 
            print("Симпсона                 = ", (b-a)/6*(function(f,a) + function(f,b) +4*function(f,(a+b)/2)), " -   ",abs((b-a)/6*(function(f,a) + function(f,b) +4*function(f,(a+b)/2))-(function(F,b) - function(F,a))) )
            print("3/8                      = ", (b-a)/8*(function(f,a) + function(f,b) +3*function(f,a+(b-a)/3)+3*function(f,a+2*(b-a)/3)), " -  ",abs(-(function(F,b) - function(F,a))+ (b-a)/8*(function(f,a) + function(f,b) +3*function(f,a+(b-a)/3)+3*function(f,a+2*(b-a)/3))) )
            print("_______________________________________")
def SKF_Left_triangle(f,m, a ,b ):
    F = integrate(f,x) 
    h = (b - a) / m 
    result = 0 
    for j in range(0,m): 
        result += function(f,a+j*h)
    result *= h 
    print("CКФ Левого треугольника  = ", result , " - абс.погр. - ",abs(result-(function(F,b) - function(F,a))), end = '' )
    print("   Теор.погр. = ", 1/2*(b-a)*h**1*MAX_f(f_diff(f,1),a,b))
    return result 
def SKF_Right_triangle(f,m, a ,b ): 
    F = integrate(f,x)
    h = (b - a) / m 
    result = 0 
    for j in range(0,m): 
        result += function(f,a+(j+1)*h)
    result *= h 
    print("CКФ правого треугольника  = ", result , " - абс.погр. - ",abs(result-(function(F,b) - function(F,a))) , end = '' )
    print("   Теор.погр. = ", 1/2*(b-a)*h**1*MAX_f(f_diff(f,1),a,b))
     
    return result 
def SKF_Middle_triangle(f,m, a ,b ): 
    F = integrate(f,x)
    h = (b - a) / m 
    result = 0 
    for j in range(0,m): 
        result += function(f,a+(j+1/2)*h)
    result *= h 
    print("CКФ среднего треугольника = ", result , " - абс.погр. - ",abs(result-(function(F,b) - function(F,a))) , end = '')
    print("   Теор.погр. = ", 1/24*(b-a)*h**2*MAX_f(f_diff(f,2),a,b))
    return result 
def SKF_Trapezoid(f,m, a ,b ): 
    F = integrate(f,x)
    h = (b - a) / (m) 
    result = 0 
    for j in range(0,m): 
        result += (function(f,a+j*h) + function(f,a+(j+1)*h))/2
    result *= h
    print("CКФ трапеции              = ", result , " - абс.погр. - ",abs(result-(function(F,b) - function(F,a))) , end = '')
    print("   Теор.погр. = ", 1/12*(b-a)*h**2*MAX_f(f_diff(f,2),a,b))
    return result 
def SKF_Simpson(f,m, a ,b ): 
    F = integrate(f,x)
    h = (b-a)/(m)
    result = 0
    for j in range(0,m): 
        result += function(f,a+j*h) + 4*function(f,a+(j+1/2)*h) + function(f,a+(j+1)*h)
    result *= h/6
    print("CКФ симпсона              = ", result , " - абс.погр. - ",abs(result-(function(F,b) - function(F,a))) , end = '')
    print("   Теор.погр. = ", 1/2880*(b-a)*h**3*MAX_f(f_diff(f,3),a,b))
    return result 
def integrate_SKF(list_f):
    m = l * int(input("Введите число промежутков деления "))
    list_SKF = [SKF_Left_triangle ,SKF_Right_triangle,SKF_Middle_triangle,SKF_Trapezoid,SKF_Simpson]
    for f in list_f :  
        F = integrate(f,x) 
        print("_______________________________________")
        print("Точное значение интеграла для функции \n  ",f," \nНа промежутке [",a,",",b,"]    =   ", function(F,b) - function(F,a))
        print("_______________________________________") 
        for k in list_SKF: 
            k(f,m ,a,b) 
l = 1 
a,b = 0,2  

list_f = [x**0, x**1 ,x**2, x**3, x**4, x**3+sin(x)]
i = 1
choise = 0 
while(choise != '0') :
    ''' Заготовка для вычисления погрешности по принципу рунге''' 
    
    i =  1 
    print("Меню  \n 1 - КФ \n 2 - СКФ \n 3 - дополнить список интегрируемых функций ")
    print(" 4 - отобразить список интегрируемых функций и пределы интегрирования   \n 5 - изменить пределы интегрирования \n 0 - завершить работу программмы")
    print(" 6 - оценка погрешности по принципу Рунге ")
    print("-1 - отчистить список функций ")
    choise = int(input())
    if choise == -1 : 
        list_f.clear() 
        print("Список функций отчищен!")
    elif choise == 0 : 
        break 
    elif choise == 1 :  
        integrate_KF(list_f)
    elif choise == 2 : 
        integrate_SKF(list_f)
    elif choise == 3 : 
        while(i != '0'):
            print("Введите функцию для интегрирований(по x) , по окончании вывода введите 0")
            i = input()
            if(i != '0') :
                list_f.append(sympify(i)) 
    elif choise == 4 : 
        print(list_f) 
        print("[" , a ," , " ,b, "]")
    elif choise == 5 : 
        a = float(input("Введите левый предел\n"))
        b = float(input("Введите правый предел\n"))
        print("Готово, пределы изменены")
    elif choise == 6 : 
        m = int(input("Введите количество делений промежутка"))
        l = int(input("Введите l(уменьшаем длину промежутка в l раз)"))
        print(list_f)
        print("Введите номер функции (от 0 до ", len(list_f) - 1 , ")")
        while(True): 
            i = int(input())
            if i in (0 , len(list_f) - 1 ):
                break 
            else : 
                print("Ввод некорректен, введите повторно")
        i = list_f[i] 
        F = integrate(i,x)
        print("Точное значение интеграла  " , function(F,b) - function(F,a))
        print("Оценка погрешности по принципу рунге для левого треугольника" , 1/(l**1-1)*(l**1*SKF_Left_triangle(i,m*l,a,b)-SKF_Left_triangle(i,m,a,b)))
        print("Погрешность = " , (function(F,b) - function(F,a)) - 1/(l**1- 1)*(l**1*SKF_Left_triangle(i,m*l,a,b)-SKF_Left_triangle(i,m,a,b)))

        print("\n")
        print("Оценка погрешности по принципу рунге для правого треугольника" , 1/(l**1- 1)*(l**1*SKF_Right_triangle(i,m*l,a,b)-SKF_Right_triangle(i,m,a,b)))
        print("Погрешность = " , (function(F,b) - function(F,a)) - 1/(l**1- 1)*(l**1*SKF_Right_triangle(i,m*l,a,b)-SKF_Right_triangle(i,m,a,b)))

        print("\n")
        print("Оценка погрешности по принципу рунге для среднего треугольника" , 1/l**2*((l**2-1)*SKF_Middle_triangle(i,m*l,a,b)-SKF_Middle_triangle(i,m,a,b)))
        print("Погрешность = " , (function(F,b) - function(F,a)) - 1/(l**2-1)*((l**2)*SKF_Middle_triangle(i,m*l,a,b)-SKF_Middle_triangle(i,m,a,b)))

        print("\n")
        print("Оценка погрешности по принципу рунге для трапеции" , 1/(l**2-1)*(l**2*SKF_Trapezoid(i,m*l,a,b)-SKF_Trapezoid(i,m,a,b)))
        print("Погрешность = " , (function(F,b) - function(F,a)) - 1/(l**2-1)*(l**2*SKF_Trapezoid(i,m*l,a,b)-SKF_Trapezoid(i,m,a,b)))

        print("\n")
        print("уточненное значение по принципу рунге для симпсона" , 1/(l**4-1)*(l**4*SKF_Simpson(i,m*l,a,b)-SKF_Simpson(i,m,a,b)))
        print("Погрешность = " , (function(F,b) - function(F,a)) - 1/(l**4-1)*(l**4*SKF_Simpson(i,m*l,a,b)-SKF_Simpson(i,m,a,b)))



