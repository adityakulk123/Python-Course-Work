#for row in range(3):
 #   for col in range(5):
      #  print(col,end='')
    #print()  


#for row in range(5):
 #   for col in range(5):
  #      print('*',end=' ')
   # print()  

#for row in range (5):
 ##      print(int((row+col)%2==0),end=' ')
   # print()





#for row in range (5):
 #   for col in range (5):
  #      print(col%2,end=' ')
   # print()

#c=1
#for row in range(5):
 #   for col in range(5):
  #      print(c,end='  ')
   #     c+=1
    #print()


#for row in range(5):
 #   for col in range(5):
  #      print(row*col,end='  ')
   # print()



#n=(int(input("enter the number: ")))
#for row in range(5):
 #   for col in range(row+1):
  #      print('*',end=' ')      
   # print()

n=(int(input("enter the number: ")))
for row in range(5):
    for col in range(n-row):
        print('*',end=' ')      
    print()