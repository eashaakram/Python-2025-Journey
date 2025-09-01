#Game
secret = 9
print("\tWelcome to the Game!")
print("Guess Any Number")
guess = int(input("Enter number: "))
if guess == secret:
    print("You are right.\nCongratulation, You won!!")
else:
    print("You are wrong.\nSorry, You loss!!")