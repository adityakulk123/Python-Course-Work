'''
n=10

for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
'''
'''
n=4
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()
    '''

'''
count=0 
n=int(input("enter the number: "))
for i in range (1,n+1):
    if n%i==0:
      count+=1

if count==2:
        print("prime")
else :
       print("not a prime")

'''
'''
count=0 
r=[]
for num in range (2,101):
    count=0
    for i in range (1,num+1):
        if num%i==0:
            count+=1

    
    if count==2:
         r.append(num)

   print(r)
   '''



prime_numbers = [num for num in range(2,1001) if len([i for i in range(1,num+1) if num%i==0])==2]
print(prime_numbers)