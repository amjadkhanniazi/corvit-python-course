# class Dog:
#     species = 'Dogesh'
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         return f'{self.name} is barking'
    
#     def description(self):
#         return f'{self.name} is {self.age} years old'



# dog1 = Dog("Mark", 4)
# dog2 = Dog("marry", 3)

# print(dog1.bark())
# print(dog1.description())
# print(dog2.bark())
# print(dog2.description())
# print(Dog.species)

# Bank Account Example
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
        print(f'{self.owner}\'s Account Created, with Balance: {self.balance} ')
    
    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            return f'Deposited Amount: {amount}, New Balance: {self.balance}'
        return 'Invalid Amount'
    def withdraw(self, amount):
        if 0 < amount <=self.balance:
            self.balance -= amount
            return f'Amount Withdrawn: {amount}, New Balance: {self.balance}'
        return 'Insufficient Balance or Invalid Amount'
    def get_balance(self):
        return f"{self.owner}'s Balance: ${self.balance}"
    
account = BankAccount("Amjad", 89000)
account1 = BankAccount('Mehwish', 100)

print(account.deposit(8900))
print(account.withdraw(33000))
print(account.get_balance())
print(account1.get_balance)