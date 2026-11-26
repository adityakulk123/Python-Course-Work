#print 1 to 10 
'''
def display(n):
    if n>10:      
       return
    print(n)
    display(n+1)
    

display(1)  
'''
'''
# print 10 to 1 in reverse order 
def display(n):
    if n>10:      
       return
    display(n+1)
    print(n)

display(1)  
'''




'''
def display(n):
    if n==len(s):
        print()
        return 
    print(s[n],end=' ')
    display(n+1)
    print(s[n],end=' ')

s='python programming'
display(0)
'''
'''    
def display(n):
    if n==len(s):
        
        return
    print(s[:n+1])
    display(n+1)

s= 'python'
display(0)
'''











'''
def display(n,w):
    if n>len(s)-w:
        return
    print(s[n:n+w])
    display(n+1,w)

s='codegnan'
display(0,2)
   '''
'''
def display(n):
    if n <1:
        return 0 
    return n + display(n-1)

print(display(10))      
'''
'''
def factorial(n):
    if n<1:
        return 1
    return n*factorial(n-1)

print(factorial(4))
'''

'''
def sumoflst(n):
    if n==len(a):
        return 0
    return a[n]+ sumoflst (n+1)

a=[1,2,3,4,5,6,100]
print(sumoflst(0))
'''


def display(n,w):
    if n>len(s)-w:
        return
    print(s[n:n+w])
    display(n+1,w)

s='codegnan'
display(0,3)