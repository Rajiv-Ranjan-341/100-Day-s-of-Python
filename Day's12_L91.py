import random
number = random.randint(1,50)
print("!!****************Welcome to the number guessing game🎰****************!!")
print("I'm thinking of a number between 1 and 50.")
game_difficulty = input("Choose a difficulty level 'easy🍳' or 'hard👷': ").lower()

def lets_play(guess_left):
    while guess_left>0:
        guess_left -= 1
        guess_number = int(input("Guess the number🔍: "))

        if guess_number == number:
            print("Congratulations🎉, you guessed it!")
            break
        elif guess_number > number:
            print("Too high👆!")
            print(f"You have {guess_left} ❤️ attempts to guess a number.")
        elif guess_number < number:
            print("Too low👇!")
            print(f"You have {guess_left} ❤️ attempts to guess a number.")
        else:
            print("I'm thinking.")



    if guess_left == 0:
        print("!!***************Game over***************!!")





if game_difficulty == 'easy':
    print("You have 10 attempts to guess the number.")
    lets_play(10)
elif game_difficulty == 'hard':
    print("You have 5 attempts to guess the number.")
    lets_play(5)

else:
    print("Invalid difficulty level.")
