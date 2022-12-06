import random

exit = False
user_score = 0
computer_score = 0

while not exit:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "exit":
        print("Goodbye!")
        exit = True

    elif user_input == computer_input:
        print("You chose", user_input)
        print("Computer chose", computer_input)
        print("It's a tie!")

    elif user_input == "rock":
        if computer_input == "scissors":
            print("You chose", user_input)
            print("Computer chose", computer_input)
            print("You win!")
            user_score += 1
        else:
            print("You chose", user_input)
            print("Computer chose", computer_input)
            print("You lost!")
            computer_score += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("You chose", user_input)
            print("Computer chose", computer_input)
            print("You win!")
            user_score += 1
        else:
            print("You chose", user_input)
            print("Computer chose", computer_input)
            print("You lost!")
            computer_score += 1

    elif user_input == "scissors":
        if computer_input == "paper":
            print("You chose", user_input)
            print("Computer chose", computer_input)
            print("You win!")
            user_score += 1
        else:
            print("You chose", user_input)
            print("Computer chose", computer_input)
            print("You lost!")
            computer_score += 1

    elif user_input not in options:
        print("Invalid choice")

    print("Your score is:", user_score)
    print("Computer score is:", computer_score)