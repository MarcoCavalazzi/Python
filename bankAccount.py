"""
Simple example of class generation ad use in Python.
"""

class BankAccount(object):
  balance = 0
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "This account belongs to %s. Balance: %.2f" %(self.name, self.balance)
  
  def show_balance(self):
    print "%.2f" %self.balance
  
  def deposit(self, amount):
    if amount <= 0:
      print "Error: amount <= 0"
      return
    else:
      print "Depositing %.2f" %amount
      self.balance += amount
    
  def show_balance(self):
    print "Balance: ",self.balance
  
  def withdraw(self, amount):
    if amount > self.balance:
      print "Error: amount greater than balance"
      return
    else:
      print "withdrawing %.2f" %amount
      self.balance -= amount
      self.show_balance()
      
my_Account = BankAccount("AccountName")
print my_Account
my_Account.show_balance()
my_Account.deposit(2000)
my_Account.withdraw(1000)

print my_Account