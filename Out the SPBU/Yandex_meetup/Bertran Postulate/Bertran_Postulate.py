from math import sqrt 
def num_simple(number): 
    if number == 2 or number == 3 or number == 5 : 
       return 1 
    if number % 2 == 0  or number % 3 == 0 :
       return 0 
    for i in range(1, int(sqrt(number/6))+1 ): 
        if(number == 6*i-1 or number == 6*i+1):
            return 1 
        if(number%(6*i-1) == 0 ) or (number%(6*i+1)) == 0 :
            return 0 
    return 1 
     
f = open("input.txt") 
f = int(f.read())
count_simple = 0 

for i in range(f+1,2*f):
    if(num_simple(i) == 1):
        count_simple+=1 
    i+=5 
print(count_simple) 
f = open("output.txt", "w") 
f.write(str(count_simple)) 


