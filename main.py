
#created class for each transaction attribute 
class transact:
    def __init__(self, transID, transName, date, type, describe, amount):
        self.transID = transID
        self.transName = transName
        self.date = date
        self.type = type
        self.describe = describe
        self.amount = amount

    def __str__(self):
        return f"{self.transID}, {self.transName}, {self.date}, {self.type}, {self.describe}, R{self.amount}"

transact1 = transact(1701, "Salary", "31-07-2026", "Income", "Monthly Salary", 10000)
transact2 = transact(1602, "Rent", "01-08-2026", "Transfer", "Monthly Rent", 3500)
transact3 = transact(1603, "Woolworths", "01-08-2026", "Purchase", "Handbag", 500)
transact4 = transact(2201, "Fiverr", "31-07-2026", "Income", "Freelance Salary", 2500)
transact5 = transact(3302, "Paballo", "02-08-2026", "Withdrawal", "Sis Groceries", 500)
transact6 = transact(1003, "Foschini", "05-08-2026", "Payment", "Account", 300)

#List of the transactions
transactions = [transact1, transact2, transact3, transact4, transact5, transact6]

#loop for printing each transaction in the list
for transaction in transactions:
    print(transaction)
    
#function to calculate the total income recieved
def total_income(transactions):
    total = 0

    for transaction in transactions:
        print(transaction.type, transaction.amount)
        if transaction.type == "Income":
            total += transaction.amount

    return total

print(total_income(transactions))

