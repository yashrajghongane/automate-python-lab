# This is the Guess Number Game
import random,sys
secreat_num = random.randint(1,20)
print("I am thinking a number between 1 to 20")

# Ask the player to guess 6 times
for guess_taken in range(1,7):
    guess = int(input("Take a Guess : "))
    if guess < secreat_num:
        print("Your Guess is too low.")
    elif guess > secreat_num:
        print("Your Guess is too High.")
    else:
        break

if guess == secreat_num:
    print("Good job! You got it in " + str(guess_taken) + " guesss.")
else: 
    print("Nope, the Number was "+ str(guess) + ".")
