from bank_account import BankAccount
class EnhancedBankAccount(BankAccount):
    def __init__(self, initial_balance=0, interest_rate=0.05):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.account_balance * self.interest_rate
        self.account_balance += interest


