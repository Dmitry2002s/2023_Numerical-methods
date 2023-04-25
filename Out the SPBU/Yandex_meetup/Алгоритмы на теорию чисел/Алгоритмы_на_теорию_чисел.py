def num_simple(number):
    for i in range(2, int(number/2)+1 ): 
        if(number%i == 0 ):
            return 0 
    return 1 
     
f = open("input.txt") 
f = int(f.read())
print(f) 

for i in range(2,f):
    if(num_simple(i) == 1) : 
        if(num_simple(f-i) == 1) : 
            print(i,f-i)
            s = open("output.txt","w") 
            s.write(str(i) + str(" "))
            s.write(str(f-i))

            break 