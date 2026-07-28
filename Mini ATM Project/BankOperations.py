#BankOperations.py
from Menu import Menu

class Operations:
    def __init__(self):
        self.base_Amt = 1500.00
    try:
        def account_details(self):
            print("Your account details:")
            print("*" * 50)
            print("Account Holder Name: Sagar")
            print("Account Number: XXXX XXXX XXXX 1356")
            print("Phone Number: XXXXXXXX96")
            print("Bank Name: SBI")
            print("Bank IFSC Code: SBIPK54F00")
            print("Bank Branch: Prakkilanka")
        def credit(self):
            credit_amt = float(input("Enter your credit amount: "))
            if credit_amt > 0:
                self.base_Amt += credit_amt
                print(f"{credit_amt:.2f} credited successfully.")
            else:
                print("Deposit amount must be greater than 0.")
        def debit(self):
            debit_amt = float(input("Enter your debit amount: "))
            if debit_amt <= 0:
                print("Amount must be greater than 0.")
            elif debit_amt <= self.base_Amt:
                self.base_Amt -= debit_amt
                print(f"{debit_amt:.2f} debited successfully.")
            else:
                print("Insufficient balance.")
        def display_amt(self):
            print(f"{self.base_Amt:.2f}")

        def exit(self):
            pass

    except ValueError:
        print("Don't enter alpha numeric values or special characters.")

base_Amt = 1500.00