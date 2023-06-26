from datetime import date
from Transaction import Transaction


class BankAccount:

    def __init__(self, name, initialBalance):
        accountNumberSeed = 1234567890
        allTransactions = []
        self.Number = accountNumberSeed
        self.Owner = name
        self.Balance = initialBalance
        self.Transactions = allTransactions

    def makeDeposit(self, amount, date, note):
        if amount < 0:
            raise Exception("Amount must be positive")

        deposit = Transaction(amount, date, note)
        self.Transactions.append(deposit)
        self.Balance += amount

    def makeWithdrawal(self, amount, date, note):
        if amount <= 0:
            raise Exception("Withdrawal must be greater than 0")

        if (self.Balance - amount < 0):
            raise RuntimeError("Insufficient funds to make withdrawal")

        withdraw = Transaction(amount, date, note)
        self.Transactions.append(withdraw)
        self.Balance -= amount

    def getBalance(self):
        return self.Balance

    def getLatestTransaction(self):
        if self.Transactions:
            latest_transaction = self.Transactions[-1]
            return latest_transaction.Amount
        else:
            return None


account = BankAccount("Bison", 0)
print(
    f'Account {account.Number} created for {account.Owner} with {account.Balance} initial Balance')

account.makeDeposit(200, "2023-06-25", "Yessir")
account.makeDeposit(600, "2023-06-25", "Dinner")
account.makeWithdrawal(1000, "2023-06-25", "Broke")

latest_amount = account.getLatestTransaction()
balance = account.getBalance()


print(latest_amount)
print(balance)

# print(date.today())
