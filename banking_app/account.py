# Will handle account logic
#eg. getting, updating accounts.
import json
import os,sys
from decorators import log

@log
def get_account(id_no):
    filename = f"accounts/{id_no}.json"
    
    if not os.path.exists(filename):
        print(f"Account with id no: {id_no} does not exist")
        return None
    
    with open(filename, "r") as file:
        account=json.load(file)
        print(account)
    return account

# get_account(id_no="223344")
@log
def create_account(id_no, name, password ):
    
    #validations, id_no, name
    if get_account(id_no):
        print(f"Account with idno {id_no} already exists")
        return None

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
    return account
# create_account(id_no="2345678", name="Peter Mwangi", password="patrilance15")