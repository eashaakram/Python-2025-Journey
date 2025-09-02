#discount
amount = int(input("Enter amount: "))
if amount >= 1000:
    print("You'r qualified for discount!")
    customer_type = input("Are you member(y/n): ")
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