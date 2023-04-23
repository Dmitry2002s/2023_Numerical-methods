
f = open('input.txt')
n,m = f.read().split() 
n,m = int(n),int(m)
result = n 
s = m 
if(n<m): # A will me more than B  
    c = n
    n= m
    m = c   
A = n
B = m 
GCD = m 
while(n%m!=0):
    GCD = n% m 
    n= m 
    m = GCD 
result = int(A*B/s/GCD)
f = open('output.txt', 'w') 
f.write(str(result))