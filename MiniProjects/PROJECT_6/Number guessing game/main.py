#NUMBER GUESSING GAME

#importing random module

import random
a = random.randint(1,51) # use randint to pick an integer between 1-50 
guesses = 0 # To track the number of guesses
while True: # while True because we don't know how many attempt we need to find that number chosen by the computer 
    guesses +=1 
    s = int(input("Guess the number : "))
    if (s > a) :
        print("lower the number please")
    elif(s == a) :
        print("you guess it right !")
        break
    else :
        print("Higher the number please")

print(f" you guess the number {a} correctly in {guesses}")