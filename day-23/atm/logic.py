data={
    123456:{"pin":1234,"balance":5000,"transaction":[]},
    123457:{"pin":1235,"balance":5500,"transaction":[]},
    123458:{"pin":1236,"balance":6000,"transaction":[]},
    123459:{"pin":1238,"balance":6500,"trancation":[]}
}

def login():
    global acc_num
    acc_num = int(input("enter the number: "))
    pin = int(input("enter the pin: "))
    if acc_num in data and data[acc_num]["pin"]==pin:
        print("login successful")
        return True
    else:
        print("Invaild login")
        return False


def menu():
    print()
    print('[C]heck balance')
    print('[D]eposit')
    print('[w]ithdraw')
    print('[T]ransactions')
    print('Change [P]in')
    print('[E]xit')

def checkbalance():
    print(f"current Balance is {data[acc_num]['balance']}")

def deposit():
    amount = int(input("enter the amount: "))
    data[acc_num]["balance"]+=amount 
    data[acc_num]["transaction"].append(f'deposit: ${amount}/-')
    print(f"{amount} is deposited successfully")

def withdraw():
    amount = int(input("enter the amount: "))
    if [acc_num]["balance"]>=amount:
        data[acc_num]["balance"]-=amount
        data[acc_num]["transaction"].append(f'withdraw: ${amount}/-')
        print(f"{amount} is withdraw successfully")
    else:
        print("insuffiecent Balance")

def transaction():
    if data[acc_num]["transaction"]:
        print("-----------------------Transactions History--------------")
        for i in  data[acc_num]["transaction"]:
            print(i)
    else:
        print("no transaction yet")

def changepin():
    pass
             