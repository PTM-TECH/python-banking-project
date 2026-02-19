# → deposit, withdraw, and balance logic
from account import create_account, get_account, update_account
from decorators import log
from time import sleep
from datetime import datetime
@log
def new_account(trials=0):
    if trials >3:
        print("Maximum retry reached. Exiting...")
        return None
    print("-"*30)
    print("Welcome to Soft Bank")
    print("Create Account")
    print("-"*30)
    id_no = input("Enter id no: ")
    account = get_account(id_no)

    if account:
        seconds=trials+2
        print(f"Id number already in use. Try again in {seconds} s")
        sleep(seconds)
        new_account(trials=trials+1)
        return
    name= input("Enter name: ")
    password = input("Enter your password: ")
    account=create_account(name=name, password=password, id_no=id_no)

    if account:
        print("-"*30)
        print(f"Welcome {account["name"]}. \nAccount Created Successfully!")
        print("-"*30)
        return get_account

# new_account()
@log
def deposit(account):
    transaction_history = account["transaction_history"]
    balance=account["balance"]
    print(f"Account balance is {account["balance"]}")
    while True:
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Amount must be greater than 0. Kindly retry...")
                continue
            break #exit the loop if valid
        except ValueError:
            print("Error! Amount must be a number(float). Kindly Retry... ")
        
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_balance = balance+amount
    transaction_history.append({"transaction_type": "Deposit", "timestamp": timestamp, "amount": amount, "balance": balance, "new_balance": new_balance})
    account["balance"]=new_balance
    account["transaction_history"]=transaction_history
    
    account_update=update_account(account=account)
    return account_update

@log
def withdraw(account):
    transaction_history = account["transaction_history"]
    balance=account["balance"]
    print(f"Account balance is {account['balance']}")
    while True:
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than 0. Kindly retry...")
                continue
            if amount > balance:
                print(f"Can't withdraw more than {balance}")
                continue
            break #exit the loop if valid
        except ValueError:
            print("Error! Amount must be a number(float). Kindly Retry... ")
        
        
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_balance = balance-amount
    transaction_history.append({"transaction_type": "Withdrawal", "timestamp": timestamp, "amount": amount, "balance": balance, "new_balance": new_balance})
    account["balance"]=new_balance
    account["transaction_history"]=transaction_history
    
    account_update=update_account(account=account)
    return account_update
# account=get_account("23232323")
# withdraw(account)
