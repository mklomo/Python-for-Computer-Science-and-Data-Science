# account.py


""" Account class definition """



from decimal import Decimal


class Account:

    """
    Account class for maintaining a bank account balance.
    """

    def __init__(self, name, balance):
        """
        Initialize an Account Object
        """

        # If balance is less than 0.00, raise an exception

        if balance < Decimal(0.00):
            raise ValueError("initial balance must be >= 0.00")

        self.name = name

        self.balance = balance


    def deposit(self, amount):

        """
        Deposit money to the account
        """

        # if amount is less than 0.00, raise an exception

        if amount < Decimal(0.00):
            raise ValueError("amount must be positive.")

        self.balance += amount


    
    def withdraw(self, amount):

        """
        Withdraw amount from the account
        """

        if amount < 0:
            raise ValueError("Enter a positive amount")

        elif amount > self.balance:
            raise  ValueError("Insufficient balance")

        self.balance -= amount