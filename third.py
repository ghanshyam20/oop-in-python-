# class BankAccount:
#     def __init__(self,owner,balance):
#         self.owner=owner
#         self.__balance=0


#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self,new_balance):
#         self.__balance=new_balance

#     def withdraw(self,amount):
#         self.__balance-=amount


#     def deposit(self,amount):
#         self.__balance+=amount




# if __name__=="__main__":
#     account=BankAccount("Alice",1000)
#     account.deposit(500)
#     account.withdraw(200)
#     print(account.owner)
#     print(account.get_balance())



# THIS IS EXAMPLE OF BOOK CLASS AND TO PRINT AUTHOR NAME AND BOOK TITLE 
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

#     def label(self):
#         return f"{self.title}-{self.author}"
    

# b=Book("clean code","Ghan")    

# print(b.label())





class Wallet:
    def __init__(self,balance:float=0):
        self.__balance=balance



    def deposit(self,amount:float):
        if amount<=0:
            raise ValueError("Deposit amount must be positive")
        
        self.__balance+=amount


    def withdraw(self,amount:float):
        if amount<=0:
            raise ValueError("withdraw amoutn must be postitive")
        
        self.__balance-=amount


    def get_balance(self)->float:
        return self.__balance
    



w=Wallet(1000)

w.deposit(500)
w.withdraw(200)


print(w.get_balance())












