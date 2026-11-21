'''
def reels():
    res = ('1-100','101-200','201-300','301-400','401-200','501-600','601-700')
    yield res[0]
    yield res[1]
    yield res[2]
    yield res[3]
    yield res[4]
    yield res[5]
    yield res[6]
    yield res[7]

feed = reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
'''
'''
def reels():
    res = ('1-100','101-200','201-300','301-400','401-200','501-600','601-700')
    for i in res:
        yield i

feed = reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))

'''
'''
def reels():
    res = ('1-100','101-200','201-300','301-400','401-200','501-600','601-700')
    for i in res:
        yield i
        
feed = reels()
for  i in feed:
    print(i)
    '''
'''
def factors(n):
    for i in range (1,n+1):
        if n%i==0:
            yield i

res = factors(18)
for i in res:
    print(i)
'''
'''
def primenumber(n):
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j==0:
               break
        else:
            yield i

res = primenumber(1700)
for i in res:
    print(i)
'''
'''
n=20

a=0
b=1
print(0,1)
for i in range (n-2):
    c=a+b 
    print(c)
    a=b
    b=c
'''


def fib(n):
    if n==1:
        yield 0 
    elif n>=2:
        a,b=0,1
        yield a 
        yield b
        for i in range(n-2):
            c=a+b
            a=b
            b=c
            yield c

res = fib(7)
for i in res:
    print(i)