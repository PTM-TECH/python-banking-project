# → login and user loading logic
from decorators import log
from time import sleep
from account import get_account

@log
def login(attempts=0, account_attempts=1):
    if attempts>=4:
        print("Maximum attempts reached")
        print("Account locked. Contact Customer Service")
        return None
    id_no=input("Enter your id no: ")
    # print("Bank login process")
    # print("Attempt no", attempts)
    account = get_account(id_no)
    #Denial of Service
    if not account:
        seconds=account_attempts
        print(f"... waiting for next login {seconds} seconds")
        sleep(seconds)
        login(attempts=attempts, account_attempts=account_attempts+2)
        #DOS => Denial of Service
        return None
    print ("Bank login process")
    print("Attempt no", attempts)
    password=input("Enter account password: ")
    
    if account["password"]!= password:
        print("Invalid Password or account")
        new_attempts=attempts+1
        login(attempts=new_attempts)
        return
    print("-------------------Welcome-------------------")
    print(f"{account["name"]}")
    print("---------------------------------------------")
    return True
login()