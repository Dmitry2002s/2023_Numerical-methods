
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
        print(f"{self.number : <25}{self.value : >25}") #Структура, которая хранит точку и значение в точке 
class interval(object):
    def __init__(self, X1,X2):
        self.X1 = X1
        self.X2 = X2
    def print(self): 
        print("[ ",self.X1,",",self.X2, " ]") #Структура, хранящая интервал (В нашем случае - где меняется знак(есть корень нечетной кратности))

def function(x):
    return 1 - math.exp(-x) + x**2  #1 - math.exp(-x) + x**2 #Вычисление значения функции 
f = 1 - sympy.exp(-x) + x**2 
Table = list();  #Таблица со значениями функции 

a = -7 # float(input("Введите левую границу \n")) 
b = 10 # float(input("Введите правую границу \n"))
m = 101 # int(input("Количество значений функции в таблице\n"))

p = a 
for i in range(0,m):
    Table.append( cell( p + (b - a )*i / (m-1), function( p  + (b - a  ) * i / (m-1))) ) #Заполняем функцию равноотстоящими значениями 
for i in Table: 
        i.print() #Отображаем нашу табличку 

print("\nИнтерполируемая функция f = " , f, '\n')
#Найдём участки строгой монотонности функции : 

f_diff = f.diff(x)  #Посчитали производную функции 

#print(f_diff)
f_diff2 = f_diff.diff(x)

counter = 0 #Число корней нечетной кратности 
N = 10000 #Делим отрезок
List = [] #Лист, содержащий отрезки, где ПРОИЗВОДНАЯ меняет знак 
H = (b-a)/N
X1 = a 
X2 = X1 + H 
Y1 = f_diff.evalf(subs = {x:X1}) 
while (X2 <= b):##Находим, где меняется знак и считаем число корней
    Y2 = f_diff.evalf(subs = {x:X2})
    if(Y1 * Y2 < 0):
        counter+=1 
        #print("В интервале : [",X1,X2 , "] меняется знак производной ")
        interv = interval(X1,X2) 
        List.append(interv)
    X1=X2
    X2=X1+H 
    Y1 = Y2 
monotony = [] 
E = 0.0000001#Эпсилон допуск для поиска участков немонотонности 
if (len(List) == 0):
    #print("Функция строго монотонна на всём [",a,",",b,"]")  
    monotony.append(interval(a,b)) 
else: 
     #Эпсилон-допуск
    for i in List: 
        A = i.X1 #Левая граница 
        B = i.X2 # Правая граница 
        C = 0 #Вычисляемое третье слагаемое 
        x_0= B + (A-B)/2  #т.к. всё задано в отрицательном, то просто возьмём середину отрезка
        while (abs( B - A ) > 2 * E):
            C = B-(B-A)*f_diff.evalf(subs ={x:B})/(f_diff.evalf(subs ={x:B}) - f_diff.evalf(subs ={x:A}))
            A = B 
            B = C 
        #print("ПРиближенная точка изменения знака производной", C)
        if(len(monotony)==0):
            monotony.append(interval(a,C))
        else: 
            monotony.append(interval(len(monotony)-1, C))
       # print("Абсолютная величина невязки -", f_diff.evalf(subs ={x:C}) , "\n") #Метод секущих a
    monotony.append(interval(C,b)) 
#print("Промежутки монотонности : ")
for i in monotony:
    i.print() 
choise = 1
while (choise == 1) :
    E = float(input("Введите Е-допуск для значений\n")) #()) 
    print("Введите точку интерполирования, приблизительный аргумент которой хотите узнать ") 
    x = float(input())
    print("Введите желаемую степень интерполяционного многочлена, не выше ", m) 
    n = int(input()) 
        
    for m in monotony: 
        INTER = [] #Храним те значения, по которым интерполируем. 
        for i in Table:
            if m.X1  < i.number < m.X2:
                INTER.append(cell(i.value,i.number))
        #print("____________________________________________\nТаблица, по которой интерполируем ")
        while (n>=len(INTER)):
                print("Требуемая степень превышает или равно числу значений функции в таблице\nПовторите Ввод степени интерполяционного многочлена ")
                n = int(input())
        #for i in INTER: 
        #    i.print() 
            
        
    
        def nearest(x, List = INTER):
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
        #print("Ближайший узел = ",Z )

        ITable = [] 
        ITable.append(INTER[Z]) 
        c = n + 1  #показатель для остановки цикла, который в начальный момент равен степени многочлена 
        p = 1
        m = len(INTER)
        while (c>1): #Создание таблицы ближайших услов интерполяции по мере удаления 
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
        #print("Отсортированная по возрастанию расстояния от узла интерполяции Таблица узлов, по которым выполняем интерполирование")
        #for i in ITable :
        #    i.print() 

        #Интерполирование в форме лагранджа 
        result_L1 = 0   
        
        for k in range (0, n) :
            w = 1 # Числитель в интерполяционной формуле лагранджа 
            w_= 1 # Знаменатель 
            for i in range (0,n) :
                if(k!=i): 
                    w *= (x-ITable[i].number) 
                    w_*= ITable[k].number-ITable[i].number
       
            result_L1 += (w/w_) *ITable[k].value

        print("Значение интерполяционного многочлена в форме лагранджа в точке ",x, " = " , result_L1) 
        print("Разница интерполяционного многочлена и функции  = ", abs(function(result_L1)-x), "\n")
   
    print("_______________________________\n2ой метод решения задачи")
    result_L = 0 
    ITable = []
    
        #print("Ближайший узел = ",Z )
    V = 0 #Номер промежутка интерполяции 
    P_i = 0 #Номер наиближайшего элемента в промежутке интерполяции 
    Z = nearest(x, Table) #Хранит ближайший к точке интерполяции узел 
    for i in monotony:
        if (Z > i.X1 and Z<i.X2):
            break
        p+=1 
    
        
    ITable = [] 
    ITable.append(Table[Z]) 
    c = n + 1  #показатель для остановки цикла, который в начальный момент равен степени многочлена 
    p = 1
    m = len(Table)
    VAX = len(ITable)#Коэф окончания заполнения таблицы 
    CAX = 0 
    AAAP = 0 

    while (c>1): #Создание таблицы ближайших услов интерполяции по мере удаления 
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
            
    n = len(ITable) 
    for k in range (0, n) :
            w = 1 # Числитель в интерполяционной формуле лагранджа 
            w_= 1 # Знаменатель 
            for i in range (0,n) :
                if(k!=i): 
                    w *= (v-ITable[i].number) 
                    w_*= ITable[k].number-ITable[i].number
       
            result_L += (w/w_) *ITable[k].value
    CVA = result_L - x #решаемое уравнение для 2ого метода 
    AAAAA = []
        
    A = a
    B = b
    N = 200 #Количество отрезков, котоыре проверяем на наличие корня нечётной кратности 
    counter = 0 #Количество корней нечетной кратности 
    List = [] 
    H = (B-A)/N 
    X1 = A 
    X2 = X1 + H 
    Y1 = CVA.evalf(subs = {v:X1}) 
    while (X2 <= B):##Находим, где меняется знак и считаем число корней
        Y2 = CVA.evalf(subs = {v:X2})
        if(Y1 * Y2 < 0):
            counter+=1 
            print("В интервале : [",X1,X2 , "] меняется знак ")
            interv = interval(X1,X2) 
            AAAAA.append(interv)
        X1=X2
        X2=X1+H 
        Y1 = Y2 
    for i in AAAAA:
        A = i.X1 #Левая граница 
        B = i.X2 # Правая граница 
        C = 0 #Вычисляемое третье слагаемое 
        x_0= B + (A-B)/2  #т.к. всё задано в отрицательном, то просто возьмём середину отрезка
        kk = 0 
        while (abs( B - A ) > 2 * E or kk == 0 ):
            C = B-(B-A)*CVA.evalf(subs = {v:B})/(CVA.evalf(subs = {v:B}) - CVA.evalf(subs = {v:A}))
            A = B 
            B = C 
            kk = 1
        print("Приближенный корень  -" , C)
        print("Абсолютная величина невязки -", abs(function(C) - x) , "\n") #Метод секущих
    print("Хотите проинтерполировать другую точку ? \n 0 - нет, 1 - да")
    choise = -1 
    while(choise != 0 and choise != 1) :
        choise = int(input())
        if (choise != 0 and choise != 1):
            print("Некорректно, введите повторно") 
        if (choise == 0):
            break
