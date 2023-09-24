import random

def main ():
    random_number = random.randint(1, 50)
    tries = 0

    print("Welcome to the Guessing Game!")
    print("I picked a number between 1 and 50. Try and guess!")

    # input prompt inside the while loop to repeatedly ask for guesses until the correct number is guessed.
    while True:
        guess = int(input("Enter your guess: "))
        tries += 1

        difference = abs(guess - random_number)
    #== operator is used for equality comparison, while a single = is used for variable assignment
        if difference ==0:
            print(f"Congratulations. You figure it out in {tries} tries.")
            #use break to exit the loop
            break
        elif difference <= 1:
            print("Your guess is scalding hot")
        elif difference <= 2:
            print("Your guess is extremely warm")
        elif difference <= 3:
            print("Your guess is very warm")
        elif difference <= 5:
            print("Your guess is warm")
        elif difference <= 8:
            print("Your guess is cold")
        elif difference <= 13:
            print("Your guess is very cold")
        elif difference <= 20:
            print("Your guess is extremely cold")
        else:
            print("Your guess is icy freezing miserably cold")
        

main()
