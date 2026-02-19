# → user interface (menu system)
from auth import login
from bank import withdraw, deposit, new_account
from time import sleep

def main():
    print("Welcome to Soft Bank")
    
    print("1. Login")
    print("2. New Account")
    option=input("Select Option 1 or 2: ")
    
    if option == "2":
        acc= new_account()
        if not acc:
            main()
            return
        print("Account created. Login")
        option="1"
        
    if option != "1":
        print("Invalid option selected. Try again!")
        sleep(1)
        main()
        return
        
    account=login()
    
    if not account:
        main()
        return
    
    print("================Welcome================")
    print(f"Your account balance is {account['balance']}")
    print("Select an option")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Logout")
    option=input("Select 1 or 2 or 3: ")
    if option == "1":
        deposit(account)
        main()
        return
    if option =="2":
        withdraw(account)
        main()
        return
        

main()