
last,k = input().split()
last = int(last) 
k = int(k)
 

#roster['As'] = 3 
#print(roster['As']) 
roster = dict ()
for i in range(0,last): #Заполняем словарь массивами с ключём,соответствующим типу,содержащим координаты элемента 
    x = int(input())
    if x in roster : 
        roster[x].append(i) 
    else : 
        roster[x] = [i] 
#print('\n')
#for i in roster : 
#    for k in roster[i]: 
#        print(k) 
last = -1
k = 0 
while(1) :
    for i in roster : 
        if last != i:
            print(roster[i][0], end= ' ')
            roster[i].pop(0) 
            if (len(roster[i])==0):
                del(roster[i])
               
            last = i  
           # if(i+1 in roster ):
           #     i = i + 1 
           # else : 
           #     i = i - 1 
            break
    if k == 1 : 
            break 
    elif len(roster) == 1 or len(roster) == 0 : 
        k = 1
    


        