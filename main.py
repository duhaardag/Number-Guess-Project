import random

def number_guessing_game(min_number = 1, max_number = 100, chance= 5):

    target_number = random.randint(min_number, max_number)

    print("Welcome To Number Guessing Game!")
    print(f"Guess a number between {min_number} and {max_number}.")

    while chance > 0:
        guess = int(input("Enter your guess: "))

        if guess == target_number:
            print("Congratulations! You guessed the correct number.")
            break
        elif guess < target_number:
            chance -= 1
            if chance != 0:
                print("Guess a bigger number")
        else:
            chance -= 1
            if chance != 0:
                print("Guess a smaller number")

        
        if chance > 0:
            print(f"You have {chance} chance{'s' if chance > 1 else ''} left.")
        else:
            print("Sorry, you've run out of chances. The correct number was:", target_number)


number_guessing_game(1, 50, 5)


        
    