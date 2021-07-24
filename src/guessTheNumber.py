print("Guess The Number")

import random
x=int(input("enter a number: "))
def guess(x):
    random_number= random.randint(1,x)
    print(random_number)
    guess=0
    while guess!= random_number:
        guess=int(input(f"Enter your number between 1and {x} :"))
        if guess >random_number:
            print("Sorry,guess again value is too high")
        elif guess<random_number:
            print("Sorry,guess again the value is too low")

    print(f"oh you have guessed the number{random_number} correctly")

guess(x) 
