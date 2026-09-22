class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        if amount <= 0:
            print("مبلغ واریزی باید مثبت باشه.")
            return
        self.balance += amount
        self.history.append(f"واریز: +{amount}")
        print(f"{amount} به حساب {self.owner}واریز شد . موجودی: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("موجودی کافی نیست.")
            return
        self.balance -= amount
        self.history.append(f"یرداشت: -{amount}")
        print(f"{amount} از حساب {self.owner} برداشت شد . موجودی: {self.balance}")

    def transfer(self, other_account, amount):
        if amount > self.balance:
            print("موجودی برای انتقال کافی نیست.")
            return
        self.withdraw(amount)
        other_account.deposit(amount)
    def show_history(self):
        print(f"\n تاریخچه تراکنش های {self.owner}:")
        for h in self.history:
            print(f"   - {h}")

        


class SavingAccount(Account):

    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.history.append(f"سود: +{interest:.2f}")
        print(f"سود {interest:.2f} به حساب پس انداز {self.owner}اضافه شد. موجودی: {self.balance:.2f}")
        

class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("از سقف اضافه برداشت مجاز فراتر رفته اید.")
            return
        self.balance -= amount
        self.history.append(f"برداشت: -{amount}")
        print(f"{amount}از حساب جاری {self.owner}برداشت شد . موجودی: {self.balance}")



if __name__ == "__main__":
    savings = SavingAccount("رضا", balance=1000, interest_rate=0.1)
    checking = CheckingAccount("مریم", balance=200, overdraft_limit=150)

    savings.deposit(500)
    savings.apply_interest()

    checking.withdraw(300)
    checking.withdraw(200)

    savings.transfer(checking, 400)

    savings.show_history()
    checking.show_history()
                                     