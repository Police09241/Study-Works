class Account():
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, req):
        if req <= self.__balance:
            self.__balance = self.__balance - req
            return self.__balance