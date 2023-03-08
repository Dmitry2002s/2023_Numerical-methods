
# -*- coding: cp1251 -*-
import math 
from math import exp
import sympy 
from sympy import diff
from sympy.abc import x 
class cell (object):
    def __init__(self, number , value ):
        self.number = number
        self.value= value
    def print(self):
        print(f"{self.number : <25}{self.value : >25}") 

def function(x):
    return 1 - math.exp(-x) + x**2
def f(List) : #На вход подается цепочка аргументов x_i 
    result = 0 
    for j in range(0,len(List)): 
        A = 1 
        for i in range(0,len(List)):
            if(i!=j):
                A*=List[j].number-List[i].number
        result += function(List[j].number)/A
    return result 
choise = 1 
F = 1 - sympy.exp(-x) + x**2 ## функция на случай дифференцирования 



print("                 Задача Алгебраического интерполирования\n")
print(" Номер варианта - 9") 
print("1 - exp(-x) + x**2")
print("Введите число значений функции в таблице") 
m = int(input()) #Число значений в таблицы
print("Введите левую границу значений функции в таблице ")
L_border = float(input()) #Левая граница 
print("Введите правую границу значений функции в таблице")
R_border = float(input()) #Правая 
Table = [] 
Run = L_border
for i in range(0,m):
    Table.append(cell(Run,function(Run) ))
    Run += (R_border - L_border)/(m-1)
for i in Table : 
    i.print

while (choise == 1) :
    print("Введите точку интерполирования") 
    x = float(input()) 

    print("Введите желаемую степень интерполяционного многочлена") 
    n = int(input()) 
    while (n>=m):
        print("Требуемая степень превышает или равно числу значений функции в таблице\nПовторите Ввод степени интерполяционного многочлена ")
        n = int(input()) 

    def nearest(x, List = Table):
        MIN = 2147483647
        l = 0 ##Вспомогательное число, которое пробегает по массиву
        Z = 0 ##Хранит номер в листе наиболее близкого элемента к x 
        for i in List : 
            if(abs(i.number-x)<MIN):
                MIN = abs(i.number-x)
                Z = l 
            l+=1
        return Z 
    Z = nearest(x) #Хранит ближайший к точке интерполяции узел 
    print("Ближайший узел = ", )
    Table[Z].print() 

    ITable = [] 
    ITable.append(Table[Z]) 
    c = n + 1  #показатель для остановки цикла, который в начальный момент равен степени многочлена 
    p = 1
    while (c>1): #Создание таблицы ближайших услов интерполяции по мере удаления 
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
    print("Отсортированная по возрастанию расстояния от узла интерполяции Таблица узлов, по которым выполняем интерполирование")
    for i in ITable :
        i.print() 

    #Интерполирование в форме лагранджа 

    result_L = 0     
    for k in range (0, n) :
        w = 1 # Числитель в интерполяционной формуле лагранджа 
        w_= 1 # Знаменатель 
        for i in range (0,n) :
            if(k!=i): 
                w *= (x-ITable[i].number) 
                w_*= ITable[k].number-ITable[i].number
       
        result_L += (w/w_) *ITable[k].value


    print("Значение интерполяционного многочлена в форме лагранджа в точке ",x, " = " , result_L) 
    print("Разница интерполяционного многочлена и функции  = ", abs(result_L - function(x)), "\n")

    result_N = 0 

    q = 1 
    ITable_N = []
    for i in range(0,n) :
        ITable_N.append(ITable[i])
        result_N+=f(ITable_N)*q 
        q*=(x-ITable_N[i].number)

    print("\nРезультат интерполяционного многочлена в форме ньютона ", result_N)
    print("Разница интерполяционного многочлена и функции  = ", abs(result_N - function(x)), "\n""\n""\n""\n")
    print("Хотите проинтерполировать другую точку ? \n 0 - нет, 1 - да")
    choise = -1 
    while(choise != 0 and choise != 1) :
        choise = int(input())
        if (choise != 0 and choise != 1):
            print("Некорректно, введите повторно") 
        if (choise == 0):
            break

        
        #/