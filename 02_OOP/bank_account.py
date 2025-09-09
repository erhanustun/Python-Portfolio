"""
---------------
Example of Object-Oriented Programming (OOP) in Python.

Concepts covered:
- Class definition
- Encapsulation (private attributes)
- Methods (deposit, withdraw, check balance)
- Dunder methods (__str__, __eq__)
"""

class BankAccount:
    def __init__(self, owner, balance=0):
        # Public attribute
        self.owner = owner
        # Private attribute (encapsulation)
        self.__balance = balance

    def deposit(self, amount):
        """Increase the account balance by amount."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        """Decrease the balance if funds are sufficient."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f" Withdrew {amount}. New balance: {self.__balance}")
        else:
            print(" Withdrawal failed. Insufficient funds.")

    def get_balance(self):
        """Return the current balance (read-only)."""
        return self.__balance

    # Dunder methods
    def __str__(self):
        """Human-readable string representation of the object."""
        return f"BankAccount(owner={self.owner}, balance={self.__balance})"

    def __eq__(self, other):
        """Compare two accounts by balance."""
        if isinstance(other, BankAccount):
            return self.__balance == other.__balance
        return False


if __name__ == "__main__":
    # Create two accounts
    acc1 = BankAccount("Alice", 100)
    acc2 = BankAccount("Bob", 200)

    print("Initial Accounts:")
    print(acc1)   # Calls __str__
    print(acc2)

    # Deposit money
    print("\n Deposit Example:")
    acc1.deposit(50)

    # Withdraw money
    print("\n Withdraw Example:")
    acc1.withdraw(30)

    # Check balance
    print("\n Balance Check:")
    print(f"{acc1.owner}'s Balance:", acc1.get_balance())

    # Compare accounts
    print("\n Equality Check:")
    print("Are accounts equal?", acc1 == acc2)  # Calls __eq__
