import random


class User():
    def __init__(self, id, name, surname, balance, accounts):
        self.id = id
        self.name = name
        self.surname = surname
        self.balance = balance
        self.accounts = accounts

    def add_account(self, account):
        self.accounts.append(account.__dict__)
    
    def update_balance(self, amount):
        self.balance = self.balance + amount
        

class Account():
    def __init__(self, transactions):
        self.id = random_id()
        self.transactions = transactions

    def add_transaction(self, transaction):
        self.transactions.append(transaction.__dict__)
     

class Transaction():
    def __init__(self, amount):
        self.id = random_id()
        self.amount = amount

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount
        }

def random_id():
    #id of 4 digits for simplicity
    return ''.join(random.choice("ABCDEFGHIJKLMNXYZ1234567890") for x in range(4))