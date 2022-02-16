class Account:
  def __init__(self, name, balance, min_balance):
    self.name = name
    self.balance = balance
    self.min_balance = min_balance
    
  def deposit(self,amount):
    self.balance += amount
  
  def withdraw(self, amount):
    if self.balance - amount >= self.min_balance:
      self.balance -= amount
    else:
      print("Sorry, not enough funds !")
      
  def statement(self):
    print(f"Account Name: {self.name}\nAccount Balance: {self.balance}")

  
  
class Current(Account):
  def __init__(self, name, balance):
    super().__init__(name, balance, min_balance = -1000)
  def __str__(self):
      return f"{self.name}'s Current Account & Balance is {self.balance}"
   
class Saving(Account):
  def __init__(self, name, balance):
    super().__init__(name, balance, min_balance = 0)

  def __str__(self):
      return f"{self.name}'s Saving Account & Balance is {self.balance}"
    
x= Current("Bibek", 500)
x.statement()
x.deposit(1500)
print(x.min_balance)
x.statement()
x.withdraw(2000)
x.statement()
x.withdraw(500)
x.statement()
print(x)
y= Saving("Bibeks", 500)
y.statement()
y.deposit(1500)
print(x.min_balance)
y.statement()
y.withdraw(2000)
y.statement()
y.withdraw(1)
y.statement()
print(y)