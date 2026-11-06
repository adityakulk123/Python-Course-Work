pin=1234

for i in range(5):
     epin = int(input("enter the pin:"))
     if epin == pin:
          print("login successful")
          break
     else:
          print("login failed")

else: 
     print("you have exeeded the maximum limits please try again after 24 hours")
