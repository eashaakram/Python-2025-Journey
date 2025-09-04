#Game
secret = 9
print("\tWelcome to the Game!")
print("Guess Any Number")
guess = int(input("Enter number: "))
if guess == secret:
    print("You are right.\nCongratulation, You won!!")
elif guess < secret:
    print("Too low! Try a bigger number.")
else:    
    print("Too high! Try a smaller number.")