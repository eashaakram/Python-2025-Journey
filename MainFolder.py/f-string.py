#f-string
letter = "Hey my name is {0} ans I am from {1}"
name = "Easha"
country = "Pakistan"
print(letter.format(name , country))
print(f"Hey my name is {name} and I'm from {country}")

price = 49.0399
txt = f"For only {price:.2f} dollars!"
print(txt.format(price = 49.0399))
print(f"{2*30}")
#to know any type of details about syntax
help("format")

#example
item_name = input("Enter name of the item: ")
price = float(input("Enter price of item: "))
quantity = int(input("Enter quantity of price: "))
cost = price*quantity
print(f"You bought {quantity} {item_name} at Rs.{price} each \nYour total bill is Rs.{cost}.")