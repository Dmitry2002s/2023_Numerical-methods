from math import sqrt


def check_simple(number : int, simple_numbers) -> bool : 
    for i in simple_numbers :
        if(number % i) == 0 : 
            return False 
    return True 

f = open('input.txt') 
f = int(f.read())
simple_numbers = [2,3]
i = 5 
result = []
while f % 2 == 0: 
    result.append(2) 
    f = f / 2
while f % 3 == 0: 
    result.append(3) 
    f = f / 3 
    
while (i <= int((f+1))) : 
    if check_simple(i, simple_numbers) == True : 
        while f % i == 0: 
            result.append(i) 
            f = f / i 
    i+=2 
    if check_simple(i, simple_numbers) == True : 
        while f % i == 0: 
            result.append(i) 
            f = f / i 
    i+=4
if check_simple(f, simple_numbers) == True : 
    simple_numbers.append(f) 
    
print(result)
k = 1
for i in result : 
    k*=i
f = open('output.txt', 'w')
final = str()
for i in range(0, len(result) - 1) : 
    final+=str(result[i]) 
    final+='*'
final+=str(result[len(result) - 1 ])
print(final)
f.write(final) 