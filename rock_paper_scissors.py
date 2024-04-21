import random

choices = ["rock", "paper", "scissors"]


def play():
    user_score = 0
    computer_score = 0
    while True:
        user_input = input("Choose : Rock/Paper/Scissors or Quit ").lower()
        if user_input == "quit":
            print("Thanks for playing!")
            break
        if user_input not in choices:
            print("Invalid input!")
            continue

        rand = random.randint(0, 2)
        computer_choice = choices[rand]
        print(f"Computer chose {computer_choice}")

        if user_input == computer_choice:
            print("Draw")
        else:
            if user_input == "rock" and computer_choice == "scissors":
                print("You win!")
                user_score += 1
                continue
            elif user_input == "paper" and computer_choice == "rock":
                print("You win!")
                user_score += 1
                continue
            elif user_input == "scissors" and computer_choice == "paper":
                print("You win!")
                user_score += 1
                continue
            else:
                print("You lose!")
                computer_score += 1
                continue

    print(f"Final result - User {user_score} : Computer {computer_score}")


start = input("Do you want to play? ").lower()
if start == "yes":
    play()
else:
    print("Bye!")
    quit()