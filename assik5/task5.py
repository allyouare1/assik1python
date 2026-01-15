class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.__owner = owner
        self.__balance = float(balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Deposit are not positive.")
        self.__balance += amount

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Withdrawal are not positive.")
        if amount > self.__balance:
            raise ValueError("Withdrawal cannot fo it balance.")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    account = BankAccount("Test User", 100)
    account.deposit(50)
    print("Current balance:", account.get_balance())