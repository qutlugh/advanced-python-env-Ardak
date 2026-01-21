class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.__owner = owner
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New Balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance

print("\n--- Task 5 Output ---")
account = BankAccount("Dave", 100)
account.deposit(50)     
account.withdraw(200)    
account.withdraw(30)     
print(f"Final Balance check: ${account.get_balance()}")