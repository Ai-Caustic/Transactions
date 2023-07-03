import datetime


class Transaction:

    def __init__(self, amount, date, note):

        self.Amount = amount
        self.Date = date
        self.Note = note

    @property
    def amount(self):
        return self.Amount

    @property
    def date(self):
        return self.Date

    @property
    def note(self):
        return self.Note


# transaction = Transaction(200, datetime.date.today, "Finance bill")

# print(transaction.amount)
