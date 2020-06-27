class BankAccount():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, deposit_amt):
        self.balance = self.balance + deposit_amt
        print("Deposit Successful. Added {} to the balance.".format(self.balance))

    def withdraw(self, withdrawal_amt):
        if self.balance >= withdrawal_amt:
            self.balance = self.balance - withdrawal_amt
            print("Withdrawal accepted. Your total balance is {}".format(self.balance))
        else:
            print("Insufficient balance.")

    def __str__(self):
        return ("Owner = {} \nBalance = {}".format(self.owner, self.balance))

bank = BankAccount("Anshi", 200)
print(bank)
bank.deposit(100)
bank.withdraw(500)

