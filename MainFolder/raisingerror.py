# #creating error
# a = int(input("Enter any value betwwn 5 & 9:"))
# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 & 9")
a = input("Enter any value between 5 & 9 (or type 'quit' to exit): ")

if a == "quit":
    print("Exiting... No error raised.")
else:
    # check if it's a number
    if a.isdigit():
        a = int(a)
        if a < 5 or a > 9:
            raise ValueError("Value should be between 5 & 9")
        else:
            print("Valid input.")
    else:
        raise ValueError("Invalid input! Enter a number or 'quit'")
