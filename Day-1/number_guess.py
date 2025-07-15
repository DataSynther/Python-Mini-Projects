## Number Guessing Game
import random

try:
    print ("Welcome to the number guessing game!")
    n = random.randrange(0,9)
    guess = int(input("Enter any number between 0 and 9: "))
    while  guess != n :
        if guess< n:
            print ("too low!")
            guess = int(input("Enter any number between 0 and 9: "))
        elif guess> n: 
            print ("too high!!")
            guess = int(input("Enter any number between 0 and 9: "))
        else:
            break
    print ("Hey!! You guessed it right!!")

except Exception as e:
    print(e)
