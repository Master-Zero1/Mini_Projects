import random

running = True
attempts = 0

while running:
    print(
        "welcome to the Guessing Game!\n"
        "Please select an option:\n"
        "1. Start Game\n"
        "2. View Stats\n"
        "3. Exit\n"
    )
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        rand_number = random.randint(1, 100)

        guess = True
        attempts = 0

        while guess:
            ask_user = int(input("Guess the number between 1 and 100: "))
            attempts += 1

            difference = abs(ask_user - rand_number)
            if ask_user == rand_number:
                print("Congratulations! You guessed the number!")
                print(f"It took you {attempts} attempts.")
                guess = False
            elif difference <= 5:
                print("You're very close! Try again.")
            elif difference <= 10:
                print("You're close! Keep trying.")
            else:
                print("You're far off! Try again.")

    if choice == "2":
        print("Viewing stats...")
        if attempts == 0:
            print("No games played yet.")
        else:
            print(f"Total attempts: {attempts}")

    if choice == "3":
        print("Exiting the game. Goodbye!")
        running = False