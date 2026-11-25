#  Number guessing game

#  Secret number
secret=7
#  The counter for amount of guesses  (Counter increases every attempt/loop)
counter=0
#  Number guessing loop
while True:
    guess=int(input("Guess: "))
    counter=counter+1
    if guess>secret:
        print("Lower")
    elif guess<secret:
        print("Higher")
    else:
        print("Correct!")
        if counter>1:
            print(f"it took you {counter} guesses")
        else:
            print(f"it took you one guess!")
        break
#  The loop doesnt stop until the input is 7, which it stops from the "break" at the end of else.