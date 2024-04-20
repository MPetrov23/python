import random


def enter_top_number():
    number = input("Enter the highest number: ")
    try:
        number = int(number)
        if number <= 0:
            print("Please enter a positive number!")
            return enter_top_number()
        else:
            return number
    except ValueError:
        print("Please enter a valid number!")
        return enter_top_number()


def play():
    max_number = enter_top_number()
    random_number = random.randint(1, max_number)
    guesses = 0

    print("Let's start!")
    while True:
        guesses += 1
        user_guess = input("Guess: ")
        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please enter a number!")
            continue

        if user_guess == random_number:
            print("Congrats! You guessed the number!")
            print("You needed {} guesses!".format(guesses))
            play_again = input("Would you like to play again? (yes/no): ")
            if play_again == "yes":
                play()
            else:
                print("Thanks for playing!")
                quit()
        elif user_guess > random_number:
            print("Too high! Guess again!")
        else:
            print("Too low! Guess again!")


play()
