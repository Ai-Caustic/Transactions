import unittest
import datetime
from Transaction import Transaction


class TestTransaction(unittest.TestCase):

    def runTest(self):
        transaction = Transaction(
            -300, datetime.datetime.now(), "Test Transaction")

        self.assertGreater(transaction.amount, 0)
