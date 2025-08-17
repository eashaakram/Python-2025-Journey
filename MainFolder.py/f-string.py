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
