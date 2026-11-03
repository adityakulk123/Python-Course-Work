
#data = ('aditya@gmail.com','aditya@123')

#gmail =input("enter the email:")
#password = input("enter the password:")

#if(gmail,password) == data:
#    print("login success")

#else:
#    print("login failed")



#seats={
 ##     's2':'available',
   #    's3':'available',
    #   's4':'booked', 
     #  's5':'available',
      # 's6':'booked'    
#}


#seatno = input("enter the seat number(sn):")

#if seatno in seats and seats[seatno] == 'available':
 #   print(f'{seatno} is booked successfully')
  #  print(seats)
#else:
 #   print(f'{seatno} is booked already')    

products={
       'laptop':{'price':23000,'stock':10},
       'mobile':{'price':15000,'stock':20},
       'mouse':{'price':1234,'stock':0},
       'keyboard':{'price':2000,'stock':40},
       'headset':{'price':3000,'stock':50}
}


search=input('enter the product name:')
if search in products and products[search]['stock']>0:
    print(f"{search} is available and the price is {products[search]['price']}")
else:
    print(f'{search} is not avialable')