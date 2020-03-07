import random

class SBI:
    IFSC="UTIB000000009"

    branch="Salt Lake"

    amount=0

    acc_number=""

    def __init__(self):
        self.acc_number=random.randint(1000,2000)
        print("Hi. Welcome to SBI")
        print("Your account number is ",self.acc_number)

    def balance(self):
        print("Your balance is ",self.amount)

    def deposit(self):
        sum=int(input("kitna jama karoge\n"))

        self.amount=self.amount+sum

        self.balance()

    def withdraw(self):
        sum=int(input("kitne chahiye\n"))

        if(self.amount>sum):
            self.amount=self.amount-sum

            self.balance()

        else:
            print("Bhikari")

rahul=SBI()

rahul.balance()
rahul.deposit()
rahul.withdraw()

