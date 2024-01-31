print("Welcome To Number Guessing Game")

number = 32

playerNumber = int(input("Guess a number between 0 and 50"))

change = 3

while True:
    if change != 0:
        if playerNumber > number:
            change -= 1
            print(change," you have the right left")
            playerNumber = int(input("choose a smaller number: ") )
            
