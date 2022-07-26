class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def userBalance(self):
        print(f"{self.name}, Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        self.balance -= amount
        return self

    def makeTransfer(self, amount, recipient):
        self.balance -= amount
        recipient.balance += amount
        print(f"{self.name}, Balance: ${self.balance}\n{recipient.name}, Balance: ${recipient.balance}")
        return self

        
joe = User('Joe', 'Joemail')
shay = User('Shay', 'Shaymail')
jose = User('Jose', 'Josemail')

joe.deposit(500).deposit(300).deposit(150).withdrawal(100)
joe.userBalance()

shay.deposit(1000).deposit(500).withdrawal(300).withdrawal(200)
shay.userBalance()

jose.deposit(5000).withdrawal(1000).withdrawal(500).withdrawal(300)
jose.userBalance()

joe.makeTransfer(100, jose)

    


























