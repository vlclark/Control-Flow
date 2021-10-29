# Developer: Vance Clark
# Date: 10/11/2021
# Program: ATM Bank Transaction

'''
This program simulates an ATM utilizing If, Elif, & Else Statements
Nesting If statements and refresh our Comparison & Logical Operators
'''

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users their names. Using variables
first_name = input("What is your first name: ")
last_name = input("What is your last name: ")

print("\nWelcome to Cash-R-Us", first_name, last_name + ", we will now set up a security PIN on your account.\n")

# Set up a pin for the users to have a secure account
pin = input("Please chose a 4-digit personal security code: ")

print("\nThank you", first_name + ", we see you set your PIN to", pin)

print("\nWould you like to make a transaction through our Automated Teller Machine")
atm = input("Yes or No: ").lower()

if atm == "yes":
    print("\n-----------------------------------------------\n")

    # This part of the program will be asking users to complete a transaction through the ATM
    print("Please insert your ATM card\n")
    print("Welcome to Cash-R-Us ATM", first_name,last_name, "\n")
    userPIN = input("What is your four digit PIN: ")

    if userPIN == pin:
        balance = 674
        print("\nYour Balance: $" + str(balance))

        # Ask users what type of transaction they want - Withdrawal/Deposit
        typeOfTransaction = input("\nWould you like to make a Withdrawal or a Deposit?\nW = Withdrawal - D = Deposit - B = Balance: ").lower()
        if typeOfTransaction == "w":
            wAmount = int(input("\nEnter amount you would like to withdrawal: "))
            balance = balance - wAmount
            print("Your updated balance is: $" + str(balance))

        elif typeOfTransaction == "d":
            dAmount = int(input("\nEnter amount you would like to deposit: "))
            balance = balance + dAmount
            print("Your updated balance is: $" + str(balance))

        else:
            print("Your balance is: $" + str(balance))

    else:
        print("\nSorry",first_name,last_name, "your PIN doesn't match our records")
        
        



else:
    print("Have a wonderful day", first_name, last_name + ", please come back and visit soon.")
