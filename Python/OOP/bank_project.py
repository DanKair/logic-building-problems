class BankAccount:
    _next_id = 1000 # Class level variable (common to all instances / objects)

    def __init__(self, owner_name, balance, account_type):
        self.id = BankAccount._next_id
        BankAccount._next_id += 1

        self.owner = owner_name
        self.balance = balance
        self.account_type = account_type

        self.transactions = []

    def deposit(self, amount: int):
        if amount <= 0:
            return "Invalid deposit amount."
        
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}. Balance: ${self.balance}")
        return f"Deposited ${amount}. New balance: ${self.balance}"

    def withdraw(self, amount: int):
        if self.balance <= 0:
             return f"Your balance: ${self.balance}, there's nothing to withdraw."
        
        elif amount > self.balance:
            return f"You can't withdraw more than ${self.balance}"  
               
        else: 
            self.balance -= amount  
            self.transactions.append(f"Withdrew ${amount}. Balance: ${self.balance}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"

    def transfer(self, amount: int, receiver_account):
        pass
        # 1. Validate transfer: if balance <= 0: return "Insufficent Balance." 
        # else: call withdraw() and deposit()

        if self.balance <= 0:
            return "Insufficent Balance." 
        else:
            self.withdraw(amount=amount)
            receiver_account.deposit(amount)
            

    def check_balance(self):
        return f"Your current balance: {self.balance }"
    
    def show_transactions(self):
        output = ["Transaction History: "]
        for index, transaction in enumerate(self.transactions):
            print(f"{index+1}. {transaction} ")
        return "\t".join(output)            

    def __str__(self):
        return f"Bank account of: {self.owner}"  

    def __repr__(self):
        return f"Bank(owner={self.owner}, balance={self.balance}, account_type={self.account_type})"     
    
# acc1 = BankAccount("John Doe", 500, "Savings")
# acc2 = BankAccount("Bob", 200, "Savings")
# print(acc1.transfer(100, acc2))
# print(acc1.check_balance())  
# print(acc2.check_balance())  

# acc1.show_transactions()
# acc2.show_transactions()


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def create_account(self, owner_name, balance, account_type):
        # 1. Create a BankAccount and append to self.accounts
        account = BankAccount(owner_name, balance, account_type)
        self.accounts.append(account)
        return self.accounts

    def find_account_by_id(self, account_id):
        # 2. Search through self.accounts for matching ID
        pass

    def list_accounts(self):
        # 3. Show summary of all accounts
        return self.accounts

bank = Bank("US Bank")
acc1 = bank.create_account("Alice", 1000,"Savings")
print(bank.list_accounts())