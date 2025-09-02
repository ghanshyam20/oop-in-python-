class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=0


    def get_balance(self):
        return self.__balance
    
    def set_balance(self,new_balance):
        self.__balance=new_balance

    def withdraw(self,amount):
        self.__balance-=amount


    def deposit(self,amount):
        self.__balance+=amount




if __name__=="__main__":
    account=BankAccount("Alice",1000)
    account.deposit(500)
    account.withdraw(200)
    print(account.owner)
    print(account.get_balance())