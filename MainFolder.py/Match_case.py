#Match case statement 
x = int(input("Enter number:"))
match x:
    case 0:
        print("case is zero")
    case 4:
        print("case is four")
    case _:
        print(x)