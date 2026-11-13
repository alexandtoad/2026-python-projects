balance = 600
ammount = 0
choice = 0
def check_balance():
    print(balance)
    choice = 0
def func_deposit():
    global balance
    ammount = int(input("How much do you want to deposit"))
    balance = balance + ammount
    print("Your balance is now £", balance)
    choice = 0
def func_withdraw():
    global balance
    ammount = int(input("How much do you want to withdraw"))
    balance = balance - ammount
    print("Your balance is now £", balance)
    choice = 0


while True:
    print("Hello welcome to atm!")
    choice = int(input("What do you want to do 1. check balance 2. deopsit 3. withdraw 4. exit"))
    if choice == 1:
        check_balance()
    if choice == 2:
        func_deposit()
    if choice == 3:
        func_withdraw()
    if choice == 4:
        print("thanks for using the atm!")
        break
    
    