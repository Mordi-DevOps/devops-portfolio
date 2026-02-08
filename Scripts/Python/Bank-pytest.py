class BankAccount:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True

class TestBankAccount:
    def test_deposit_50(self):
        b = BankAccount(1)
        assert b.deposit(50) == True, "Expected to return True"
        assert b.balance == 50, "Expected a balance of 50"

    def test_withdraw_49(self):
        b = BankAccount(2)
        b.deposit(50)
        assert b.withdraw(49) == True, "Expected to return True"
        assert b.balance == 1, "Expected a balance of 1"

a = TestBankAccount()
a.test_deposit_50()
a.test_withdraw_49()
