
'''
def display(n):
    if n>5:      
       return
    display(n+1)
    print(n)
    
n=1
display(n)
'''

'''

def display(n):
    if n>N:
        return 
    if n%2==1:
        print(n)

    display(n+1)
    

n=1
N=10
display(n)
'''

'''
def display(n):
    if n <1:
        return 0 
    return n + display(n-1)

print(display(2)) 








'''

def display(n):
    if n<1:
        return 0
    return n + display(n-1)

print(display(5))

    
        