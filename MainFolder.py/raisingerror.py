#creating error
a = int(input("Enter any value betwwn 5 & 9:"))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 & 9")