import logic as lg

if lg.login():
    print("welcome to the smartatm")
    while True:
        lg.menu()
        ch = input("enter the choice: ").upper()
        if ch=='C':
            lg.checkbalance()
        elif ch=='D':
            lg.deposit()
        elif ch=='W':
            lg.withdraw()
        elif ch=='T':
            lg.transaction()
        elif ch=='P':
            pass
        elif ch=='E':
            print("thank you , vist again")
            break
        else:
            print("invaild choice")
            break
        
