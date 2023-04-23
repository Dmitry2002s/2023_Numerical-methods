f = open('input.txt')
f = f.read()
a,b = f.split()
a = int(a)
b = int(b)
if(a<b): # A will be more than B  
    c = a 
    a = b
    b = c   
A = a 
B = b 
GCD = b 
while(a%b!=0):
    GCD = a % b 
    a = b 
    b = GCD 
result = int(A*B/GCD)
print(result)
f = open('output.txt' , 'w')
f.write(str(result)) 
