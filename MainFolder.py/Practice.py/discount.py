#discount
'''Problem Statement: Online Shopping Discount Checker
You are writing a Python program for an online shopping app
The program should: Ask the user for the total amount of their shopping
If the amount is greater than or equal to 1000, they qualify for a discount
Then ask if they are a first-time customer (yes or no)
If they are a first-time customer, they get 20% discount If not, they get 10% discount
If the amount is less than 1000, print: "No discount. Spend at least 1000 to get a discount“
'''
print(">>>> Online Shopping Discount Checker <<<<")
amount = int(input("Enter your total amount: "))
if amount >= 1000:
    print("You'r qualified for discount!")
    customer_type = input("Are you first customer(y/n): ")
    if customer_type == 'y':
        print("You will get 20% discount")
        discount = amount * 0.2
        new_amount = amount - discount
        print(f"New amount is {new_amount}")
    else:
        print("You will get 10% discount")
        discount = amount * 0.1
        new_amount = amount - discount
        print(f"New amount is {new_amount}")
else:
    print("No discount for you.\nSpent atleast 1000 rupees to get a discount")