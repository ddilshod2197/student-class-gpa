class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Depozit summasi 0 dan katta bo'lishi kerak")
```

```python
# Test qilish
account = BankAccount(100)
print(account.balance)  # 100

account.deposit(50)
print(account.balance)  # 150

try:
    account.deposit(-20)
except ValueError as e:
    print(e)  # Depozit summasi 0 dan katta bo'lishi kerak
