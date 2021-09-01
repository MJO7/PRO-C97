import random
n = random. randint(0,9) 
i = 0
print("Number Guessing Game")
print("Guess a number between 0 and 9")
while i<5 :
    yourGuess = int(input("Enter your guess:-"))
    if yourGuess==n :
        print("You guessed the correct number!")
        print("You won!")
        i=100
    
    elif yourGuess>n:
        print("Guess a number lower than that.")
        i=i+1

    else:
        print("Guess a number higher than that.")
        i=i+1
if i==5:
    print("You lost! The number is",n)





