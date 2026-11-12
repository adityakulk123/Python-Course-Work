n = int(input("Enter the size: "))
m= n//2
for i in range(n):
    for j in range(n):    
        if i ==0 or j==0 or i ==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()