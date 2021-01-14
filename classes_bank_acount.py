class Account:
    def __init__(self,name,balance):

        self.name = name
        self.balance = balance
        print("Account owner:" + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 & (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Cannot not withdraw: £" + str(amount) + "; insufficient funds")

    def show_balance(self):
        print("Balance is £{}".format(self.balance))


if __name__ == '__main__':
    James = Account("James", 0)
    James.show_balance()

    James.deposit(1000)
    James.show_balance()
    James.withdraw(1750)
    James.show_balance()
