

f = open('input.txt')  
f = f.read() 
a,b = f.split() 

a = int(a) 
b = int(b)

GCD = 1 
if (a<b): 
    GCD = a 
    a = b 
    b = GCD 
    GCD = 1 
GCD = b 
while(a % b != 0) : 
    GCD = a % b 
    a = b 
    b = GCD 
print(GCD)
f = open('output.txt' , 'w')

f.write(str('1'*GCD)) 