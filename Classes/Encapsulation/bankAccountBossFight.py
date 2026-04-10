class BankAccount:

    def __init__(self,owner,balance,pin):

        self.owner = owner
        self.__balance = balance
        self.pin = pin

    @property
    def balance(self):
        return self.__balance

    @property
    def pin(self):
        return '****'

    @pin.setter
    def pin(self,pin):
        if isinstance(pin,int) and 1000 <= pin <= 9999:
            self.__pin = pin
        else:
            print('Invalid Pin!')
            raise ValueError('Please set proper pin')

    def deposit(self,amount,pin):
        if int(pin) == self.__pin:
            if isinstance(amount,int) and amount > 0:
                self.__balance = self.__balance + amount
                print(f'balance: {self.balance}')
            else:
                print('Amount must be greater than 0!')

        else:
            print('Wrong PIN!')

    def withdraw(self,amount, pin):
        if int(pin) == self.__pin:
            if isinstance(amount,int) and amount < self.__balance:
                self.__balance = self.__balance - amount
                print(f'balance: {self.balance}')
            else:
                print('Insufficient funds!')
        else:
            print('Wrong PIN!')

    def change_pin(self,old_pin,new_pin):

        if isinstance(new_pin,int) and 1000<=new_pin<=9999:
            if int(old_pin) == self.__pin:
                self.__pin = int(new_pin)
                print('PIN changed')
            else:
                print('Wrong old PIN')
        else:
            print('PIN must be 4 digits')



customer = BankAccount('Sai',5000,1234)

customer.deposit(1000,1234)
customer.deposit(500,9999)
customer.deposit(-100,1234)

customer.withdraw(2000,1234)
customer.withdraw(9000,1234)

customer.change_pin(1234,5678)
customer.change_pin(1234,5678)
customer.change_pin(5678,99)

customer.balance = 99999999
customer.__balance