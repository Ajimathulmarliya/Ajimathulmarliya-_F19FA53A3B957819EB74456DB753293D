# 2.1 Implement a class called BankAccount that represents a bank account. The class should have private attributes for account number, account holder name, and account balance. Include methods to deposit money, withdraw money, and display the account balance. Ensure that the account balance cannot be accessed directly from outside the class. Write a program to create an instance of the BankAccount class and test the deposit and withdrawal functionality


class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self._account_number = account_number
    self._account_holder_name = account_holder_name
    self._account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self._account_balance += amount
      print(f"Deposited ${amount}. New balance: ${self._account_balance}")
    else:
      print("Invalid deposit amount. Amount must be greater than 0.")

  def display_balance(self):
    print(
        f"Account Balance for {self._account_holder_name}: ${self._account_balance}"
    )


# Create an instance of the BankAccount class
account1 = BankAccount("123456789", "John Doe")

# Deposit money into the account
account1.deposit(1000)

# Display the account balance
account1.display_balance()

# Attempt to access the account balance directly (will not work)
# print(account1._account_balance)
