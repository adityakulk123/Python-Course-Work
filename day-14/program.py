'''
l=[12,9,3,4,5,10,2,4,5,2,4,5]

i=0
j=len(l)-1

while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])

    i+=1
    j-=1
    '''

'''
bill = 0

while True:
    product = input("Enter the product name(STOP):")
    if product == 'STOP':
        print("Total Bill:",bill)
        break
    price = int(input("Enter the price:"))
    quantity = int(input("Enter the quantity:"))
    bill+= price*quantity

    '''

'''
menu = {
    "Pizza": 250,
    "Burger": 120,
    "Sandwich": 100,
    "Pasta": 180,
    "French Fries": 90,
    "Coke": 50
}

print("\n========== MENU CARD ==========")
print("Product Name          Price")
print("------------------------------")

for product, price in menu.items():
    print(f"{product:<20} ₹{price}")

print("===============================")

bill = 0

while True:
 
    product = input("Enter the product name(STOP):")
    if product == 'STOP':
        print("Total Bill:",bill)
        print("=============Final Bill=============")
        print("Product Name          Price          Quantity          Total")
        print("-------------------------------------")
        print(f"{product:<20} ₹{price:<15} {quantity:<15} ₹{price*quantity}")
        
        print ("Thank you for the shooping here")
        break
    price = menu[product]
    quantity = int(input("Enter the quantity:"))
    bill+= price*quantity


'''

products = {
    'sugar':40,
    'salt' :30,
    'cooking oil ' : 120,
    'tissue' : 40,
    'soap' : 32,
    'shampoo' : 5,

}

# to display menu 

print("welcome to the store".center(50,'-'))
print("product name",'price')
for i in products:
    print(i.ljust(12,' '),':',products[i])


carts={}
while True:
    cart = input("enter the name(exit):").lower()
    if cart == 'exit':
        break
    qua = int(input("enter the quanity:"))
    carts[cart]=qua

print("Bill".center(50,'-'))
print('product Name Quanity  price')
bill=0
for i in carts :
         print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),products[i])
         bill += carts[i]*products[i]


print(f"Toatal bill: {bill}")
print("Thanks for the shapping ")      