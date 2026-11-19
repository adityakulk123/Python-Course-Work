'''
sot= lambda a,b,c: a+b+c
print(sot(10,20,30))


gst = lambda price: price+price*0.18
print(gst(1000))

avg=lambda l:sum(l)/len(l)
l=[99,87,89,6,43]
print(avg(l))

iseven = lambda n :"Even" if n%2==0 else "odd"
print(iseven(10))
print(iseven(4))


isvowel = lambda ch: "vowel" if ch in ' aeiouAEIOU' else "consonant"
print(isvowel('a'))
print(isvowel('z'))

'''
'''
check= lambda data,pro: (f"product price : {data[pro]['price']}" if data [pro]["stock"]>0 else "out of stock") if pro in data else "product is unavilable" 

data = {
      'apple':{'stock':10,'price':50},
      'mango':{'stock':10,'price':30},
      'pineaple':{'stock':60,'price':40},
      'orange':{'stock':50,'price':50},
      'sapota':{'stock':0,'price':70},
       }

print(check(data,'orange'))
'''

def addten(l):
    for i in range (len(l)):
        l[i]+=10
    return l

l=[9,2,3,5,7,8,9]
print(addten(l))
'''
def domain(d):
    for i in range(len(d)):
        d[i]=(d[i].split('@')[1]).split('.')[0]
    return d 

d=['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']
print(domain(d))
'''

d=['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']
domain = list(map(lambda i:(i.split('@')[1]).split('.')[0],d))
print(domain)

c=['safgh','hgygj','huygbh']
cu= list(map(lambda i:i.upper(),c))
print(cu)



d={'a':20,'b':30,'c':'2300','d':'24500','e':'75000'}
gst=list(map(lambda i:i,d.items()))
print(d)

d={'a':20,'b':30,'c':2300,'d':24500,'e':75000}
gst = dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
print(gst)


l=[1,2,3,4,5,6,7,8,64,53,54,76,100]
even=list(filter(lambda i:i%2==0,l))
print(even)


a=['a','d','f','g','h','h','y','u']
vowels = list(filter(lambda i: i in 'aeiouAEIOU',a))
print(vowels)


from functools import reduce 

l=[2,45,6,5,7,3,5]
sumofl = reduce(lambda sum,i:sum+i,l)
print(sumofl)


l=[2,45,6,5,7,3,5]
sumofl = reduce(lambda max,i:max if max<i else i,l)
print(sumofl)