# ATM System
import sys

print("_" * 20,end="")
print(" ATM System ",end="")
print("_" * 20,end="\n")
print()
# requirements = bal,deposit,withdraw,exit
balance = 0 # current balance is 0

def check_bal():
    return balance

def deposit(amount):
    global balance
    balance += amount
    return amount

def withdraw(amount):
    global balance
    balance -= amount
    return amount

def atm_logic():
    try :
        while True:
            print("1. Check Balance ")
            print("2. Deposit ")
            print("3. Withdraw ")
            print("4. Exit ")
            try:
                choice = int(input("Enter your choice : ")) 
            except ValueError: 
                print("You have Selected wrong option, Plz Selecet correct option. ")
                print()
                continue
            if choice == 1:
                # checking account balance
                print("Your avl balance is",check_bal())
                print()
            elif choice == 2:
               # deposit money
                try:
                    amount = int(input("Enter the Amount: "))
                    if amount >= 0:
                        print(deposit(amount),"added in your account.")
                        print("Your current avl balance is",check_bal())
                        print()
                    else:
                        print("You can't enter amount in negative")
                        print()
                except ValueError:
                    print("you have entered wrong amount. try again...")
                    print()
                    continue
            elif choice == 3:
                # withdraw money
                try:
                    amount = int(input("Enter the Amount: "))
                    if amount >= 0:
                        if amount <= balance:
                            print(withdraw(amount),"withdraw from your account")
                            print("Your current avl balance is",check_bal())
                            print()
                        else:
                            print("Your current avl balance is",check_bal())
                            print("You can't withdraw this amount ",amount)
                            print()
                    else:
                        print("You can't amount in negative. ")
                        print()
                except ValueError:
                     print("you have entered wrong amount. try again...")
                     print()
                     continue
            elif choice == 4:
                break
            else: 
                print("You have Selected Wrong option, try again...")
                print()
    except KeyboardInterrupt: 
        print("you have entered wrong key!, Try Again ")
        
atm_logic()
