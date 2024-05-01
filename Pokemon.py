import random

def play_game():
    print("Welcome to my Pokemon game!")
    print("Let's play!")

    choices = ["psychic", "dark", "fighter"]

    while True:
        user_choice = input("Choose your move (psychic, dark , or fighter): ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print(f"You chose: {user_choice}")
        print(f"The computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "psychic" and computer_choice == "fighter") or
            (user_choice == "dark" and computer_choice == "psychic") or
            (user_choice == "fighter" and computer_choice == "dark")
        ):
            print("Congratulations! You win! :D happy time ")
        else:
            print("Sorry, you lose! sad time ")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

play_game()
