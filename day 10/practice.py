class BankAccount():
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    def display_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: {self.balance}")
        
account1 = BankAccount("Nischal Gautam", 1000)
account1.display_balance()
account1.deposit(2000)
