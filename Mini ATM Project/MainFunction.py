#MainFunctions.py
from Menu import Menu
from BankOperations import Operations
menu = Menu()
opr = Operations()
while True:
    try:
        menu.menuData()
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                opr.account_details()
            case 2:
                opr.credit()
            case 3:
                opr.debit()
            case 4:
                opr.display_amt()
            case 5:
                print("Thanks for using this program.")
                break
            case _:
                print("Invalid choice. Try again...!")
    except ValueError:
        print("Don't enter alpha numeric values or special characters.")