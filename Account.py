               
class Account:
    def _init_(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
    def deposit(self, amount):
        if amount <= 0:
            return "Invalid deposit amount"
        else:
            self.balance += amount
            self.deposits.append({"amount": amount, "narration": "deposit"})
            return "You have deposited KES "+str(amount)+" to "+self.name+" account number "+str(self.account_number)+". New balance is KES "+str(self.balance)+"."
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        elif self.balance < amount:
            return "Insufficient balance. Your current balance is KES "+str(self.balance)+"."
        else:
            self.balance -= amount
            self.withdrawals.append({"amount": amount, "narration": "withdrawal"})
            return "You have withdrawn KES "+str(amount)+" from "+self.name+" account number "+str(self.account_number)+". New balance is KES "+str(self.balance)+"."
    def check_balance(self):
        return "Your account balance is KES "+str(self.balance)+"."
    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            return "Sorry, you have an outstanding loan. Please repay it first."
        elif amount < 100:
            return "Loan request declined. Minimum loan amount is KES 100."
        elif len(self.deposits) < 10:
            return "Loan request declined. Please make at least 10 deposits first."
        elif amount > (sum(transaction["amount"] for transaction in self.deposits)/3):
            return "Loan request declined. Maximum amount you can borrow is one-third of your total deposits."
        else:
            self.loan_balance += amount
            self.balance += amount
            return "You have successfully borrowed KES "+str(amount)+". Your new balance is KES "+str(self.balance)+"."
    def repay_loan(self, amount):
        if amount <= 0:
            return "Invalid repayment amount"
        elif amount > self.loan_balance:
            overpayment = amount - self.loan_balance
            self.loan_balance = 0
            self.balance += overpayment
            return "Thank you for repaying your loan. Your overpayment of KES "+str(overpayment)+" has been credited to your account. Your new balance is KES "+str(self.balance)+"."
        else:
            self.loan_balance -= amount
            self.balance -= amount
            return "Thank you for repaying your loan. Your new loan balance is KES "+str(self.loan_balance)+"."
    def transfer(self, amount, destination_account):
        if amount <= 0:
            return "Invalid transfer amount"
        elif amount > self.balance:
            return "Insufficient balance. Your current balance is KES "+str(self.balance)+"."
        else:
            self.balance -= amount
            destination_account.balance += amount
            return "You have transferred KES "+str(amount)+" from "+self.name+" account number "+str(self.account_number)+" to "+destination_account.name+" account number "+str(destination_account.account_number)+". Your new balance is KES "+str(self.balance)+"."
    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        statement = ""
        for transaction in transactions:
          narration = transaction["narration"]
          amount = transaction["amount"]
          statement += f"{narration} - {amount}\n"
        return statement    
              
  
