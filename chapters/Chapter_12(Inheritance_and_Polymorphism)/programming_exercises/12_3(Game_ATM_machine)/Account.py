class Account:
    __id: int
    __balance: float
    __annual_interest_rate: float

    def __init__(self, id: int = 0, balance: float = 100, annual_interest_rate: float = 0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annual_interest_rate

    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount: float):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False

    def get_monthly_interest_rate(self):
        return self.__annualInterestRate / 12

    def get_monthly_interest(self):
        return self.__annualInterestRate * self.__balance

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def get_annual_interest_rate(self):
        return self.__annualInterestRate

    def set_id(self, id):
        self.__id = id

    def set_balance(self, balance):
        self.__balance = balance

    def set_annual_interest_rate(self, annual_interest_rate):
        self.__annualInterestRate = annual_interest_rate

    def __str__(self):
        return 'Account ID: {}, Balance: {}, Annual Interest Rate: {}'.format(self.__id, self.__balance,
                                                                              self.__annualInterestRate)

    def __repr__(self):
        return self.__str__()
