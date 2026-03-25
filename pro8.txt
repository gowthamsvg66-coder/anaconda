balance = 0
def deposit(amount):
    global balance
    balance += amount
    return balance
def withdraw(amount):
    global balance
    if amount > balance:
        raise Exception("Insufficient balance!")
    balance -= amount
    return balance
def check_balance():
    return balance