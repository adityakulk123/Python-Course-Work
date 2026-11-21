'''
n=10

for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()
'''

n=4
for i in range(1,n+1):
    for j in range(i):
        print(i,end=" ")
    print()