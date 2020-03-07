import random
number=random.randint(1,101)
guessed=int(input("Guess a number between 1-100\n"))
attempt=1
while guessed!=number:
    attempt+=1
    if guessed>number:
        print("Guess Lower")
        guessed=int(input("Guess again\n"))
    else:
        print("Guess Higher")
        guessed=int(input("Guess again\n"))
else:
    print("Woooohoooo!","You took",attempt,"attempts")
