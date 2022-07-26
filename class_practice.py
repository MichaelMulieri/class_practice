class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0

    def userBalance(self):
        print(f"{self.name}, Balance: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdrawal(self, amount):
        self.balance -= amount
        return self.balance

    def makeTransfer(self, amount, recipient):
        self.balance -= amount
        recipient.balance += amount
        print(f"{self.name}, Balance: {self.balance}\n {recipient.name}, Balance: {recipient.balance}")

        
joe = User('Joe', 'Joemail')
shay = User('Shay', 'Shaymail')
jose = User('Jose', 'Josemail')

joe.deposit(500)
joe.deposit(300)
joe.deposit(150)
joe.withdrawal(100)
joe.userBalance()

shay.deposit(1000)
shay.deposit(500)
shay.withdrawal(300)
shay.withdrawal(200)
shay.userBalance()

jose.deposit(5000)
jose.withdrawal(1000)
jose.withdrawal(500)
jose.withdrawal(300)
jose.userBalance()

joe.makeTransfer(100, jose)

    


























