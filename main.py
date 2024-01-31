print("Welcome To Number Guessing Game!")

number = 32

playerNumber = int(input("Guess a number between 0 and 50"))

chance = 3

while True:
    if chance != 0:
        if playerNumber > number:
            chance -= 1
            print(chance," you have chance left")
            playerNumber = int(input("choose a smaller number: ") )

