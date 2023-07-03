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

    def make_deposit(self, amount, date, note):
        if amount < 0:
            raise ValueError("Amount must be positive")

        deposit = Transaction(amount, date, note)
        self.Transactions.append(deposit)
        self.Balance += amount

    def make_withdrawal(self, amount, date, note):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than 0")

        if (self.Balance - amount < 0):
            raise RuntimeError("Insufficient funds to make withdrawal")

        withdrawal = Transaction(amount, date, note)
        self.Transactions.append(withdrawal)
        self.Balance -= amount

    def get_balance(self):
        return self.Balance

    def get_latest_transaction(self):
        if self.Transactions:
            latest_transaction = self.Transactions[-1]
            return latest_transaction.Amount
        else:
            return None

    def get_transaction_history(self):
        if self.Transactions:
            print("Transaction History")
            for transaction in self.Transactions:
                print(f'Amount: {transaction.Amount}')
                print(f'Date: {transaction.Date}')
                print(f'Note: {transaction.Note}')
                print("-------------------")

        else:
            print("No transaction found")

    def transaction_summary(self):
        if self.Transactions:

            total_transactions = len(self.Transactions)
            total_deposits = sum(
                transaction.Amount for transaction in self.Transactions if transaction.Amount > 0)
            total_withdrawals = abs(sum(
                transaction.Amount for transaction in self.Transactions if transaction.Amount < 0))
            average_transaction = sum(
                transaction.Amount for transaction in self.Transactions) / total_transactions
            percentage = int((sum(
                transaction.Amount for transaction in self.Transactions) / 100) * total_transactions)

            summary = {
                'Total transactions': total_transactions,
                'Total deposits': total_deposits,
                'Total withdrawals': total_withdrawals,
                'Average transaction amount': average_transaction,
                'Percentage transactions': percentage
            }
            print(f'Total Transactions: {summary["Total transactions"]}')
            return summary

            # print("TRANSACTION SUMMARY:")
            # print(f'Total transactions: {total_transactions}')
            # print(f'Total deposits: {total_deposits}')
            # print(f'Total withdrawals: {total_withdrawals}')
            # print(f'Average transaction Amount: {average_transaction}')
            # print(f'Percentage transactions: {percentage}%')
        else:
            print("No transactions found")


account = BankAccount("Bison", 1000)
print(
    f'Account {account.Number} created for {account.Owner} with ${account.Balance} initial Balance')

account.make_deposit(200, "2023-06-25", "Bought a cake")
account.make_deposit(600, "2023-06-25", "Dinner")
account.make_withdrawal(1000, "2023-06-25", "Broke")

latest_amount = account.get_latest_transaction()
balance = account.get_balance()

print(f'Latest transaction was ${latest_amount}')
print(f'Balance is ${balance}')
print("------------------")
account.get_transaction_history()
account.transaction_summary()
# print(date.today())
