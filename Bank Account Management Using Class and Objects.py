class BankAccount:
    def __init__(self, account_number, account_holder, account_type, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display(self):
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Account Type:", self.account_type)
        print("Current Balance:", self.balance)

account = BankAccount("1001", "Abhinav", "Savings", 10000)

account.display()
account.deposit(5000)
account.withdraw(3000)
account.display()