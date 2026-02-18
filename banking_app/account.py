# Will handle account logic
#eg. getting, updating accounts.
import json
import os,sys

def get_account(id_no):
    filename = f"accounts/{id_no}.json"
    
    if not os.path.exists(filename):
        print(f"Account with id no: {id_no} does not exist")
        return None
    
    with open(filename, "r") as file:
        account=json.load(file)
        print(f"Account details: {account}")
    return account

# get_account(id_no="223344")

def create_account(id_no, name, password ):
    
    #validations, id_no, name
    if get_account(id_no):
        print("Account already exists")
        sys.exit()

    account = {
        "account_no": id_no,
        "id_no": id_no,
        "name": name,
        "transaction_history":[],
        "balance": 0,
        "password": password
    }
    
    filename =f"accounts/{id_no}.json"
    
    with open(filename, "w") as file:
        json.dump(account, file, indent = 4)
    print(f"Account created successfully!")
create_account(id_no="222333444", name="Patrick Mutua", password="patrilance15")


    