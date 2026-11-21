'''
res =[i for i in range (1,11)]
print(res)

n=16
fact = [i for i in range(1,n+1) if n%i==0]
print(fact)


names=['swati','dhansree','sowmya','sreeja','siri']
resn = [i for i in names if i.startswith('s')]
print(resn)

l=[1,2,3,4,5,6,7,8,8665,7,6,5,4,54,34,54]
rese=[i if i%2==0 else 0 for i in l]
print(rese)



nes = [[j for j in range(1,4)]for i in range(5)]
print(nes)
'''
n=16
fact={i for i in range (1,n+1) if n%i==0}
print(fact)

res={i for i in range(1,11)}
print(res)

