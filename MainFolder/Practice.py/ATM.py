#ATM Machine Method
print("\tWelcome To ATM")
pin = 1234
balance = 5000
code = int(input("Enter your pin code: "))
if pin == code:
    print("Login Successfully!!\nChoose any one of them\n1)Withdraw\n2)Balance inquiry")
    choice = int(input("Enter your choice(1 or 2):"))
    #nested if else
    if choice == 1:
        amount = int(input("Enter your withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Tansaction done\nRemaining balance:",balance)
        else:
            print("Insufficient Balance")
    elif choice == 2:
        print("Your Balance:",balance)
    else:
        print("Choose number from menu")
else:
    print("Wrong pin code!")