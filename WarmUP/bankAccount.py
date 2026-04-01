class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposit successful. Balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdraw successful. Balance: {self.balance}')
        else:
            print('Insufficient funds!')

    def show_balance(self):
        print(f'{self.owner} — Balance: {self.balance}')

class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,intrest_rate):

        super().__init__(owner,balance)
        self.intrest_rate = intrest_rate

    def add_intrest_rate(self):
        self.balance = self.balance * self.intrest_rate / 100
        return self.balance

class CurrentAccount(BankAccount):

    def __init__(self,owner,balance,overdraft_limit):

        super().__init__(owner,balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self,amount):

        if amount < self.balance:
            self.balance -= amount
            print(f'Withdraw successful. Balance: {self.balance}')

        elif self.balance < amount < self.balance+self.overdraft_limit:
            self.balance -= amount
            print(f'Withdraw successful from overdraft. Balance: {self.balance}')

        else:
            print(f'OverDraft limit reached')


user1 = CurrentAccount('Ruku',10000,5000)

user1.withdraw(15000)