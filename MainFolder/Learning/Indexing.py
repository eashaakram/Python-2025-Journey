# text = "Python"
# i = 0
# while i<len(text):
#     print(f"Index{i} : {text[i]}")
#     i+=1

# test_list = [1,2,3]
# for i in range(len(test_list)):
#     print(f"value is {test_list[i]}")

# text = "Code"
# for index, char in enumerate(text):
#     print(f"Index{index}:{char}")

name = input("Enter your name: ").lower() #lower will change all characters in lower case 
vowels = "aeiou"
i = 0
found = False
vowels_found = []
while i < len(name):
    if name[i] in vowels:
        found = True
        vowels_found.add(name[i])
        i+=1
    print("Found")
    if found:
        print("Vowels used: ",",".join(sorted(vowels_found)))
    else:
        print("No vowels found")