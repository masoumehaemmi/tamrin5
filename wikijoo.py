
n = int(input("enter your number:"))
pas=[[1 for i in range(n)] for j in range(n) ] 

for i in range(0,n):
        
        for j in range(1,i):
               
               pas[i][j]=pas[i-1][j-1] + pas[i-1][j]
               
print()               
                        
for i in range(n):        
        for j in range(i+1):
                print(pas[i][j],end="   ")
                 
        print()       