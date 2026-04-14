import random
import pycountry

print("Welcome to the Antakshri !!\n")

running = True

while running:
    print(
        "Choose from the options:\n"
        "1. Start The Game\n"
        "2. How To Play The Game?\n"
        "3. Exit\n"
    )

    choice = input("Select from the options (1-3):")

    all_countries = [country.name for country in pycountry.countries]

    random_country_to_start_game = random.choice(all_countries)

    if choice == "1":
        print("Starting the game...\n")
        Current_country = random_country_to_start_game
        used_countries = set()
        used_countries.add(Current_country)
        print("The first country is:", Current_country)

        while True:
            user_input = input(
                f"Enter a country name that starts with the last letter of {Current_country}: "
            )

            # Normalize user input for case-insensitive comparison and avoid leading/trailing spaces
            normalized_user_input = user_input.strip().capitalize()

            if normalized_user_input not in all_countries:
                print("Invalid country name. Please try again.")
                continue
            elif normalized_user_input in used_countries:
                print("This country has already been used. Please try again.")
                continue

            # Check if the first letter of the user's country matches the last letter of the current country
            if Current_country.lower().strip()[-1] == normalized_user_input.lower().strip()[0]:
                print("Its correct answer")
                used_countries.add(normalized_user_input)
                
                # Check if there are any unused countries left
                unused_countries = [c for c in all_countries if c not in used_countries]
                if not unused_countries:
                    print("No unused countries left. You win!")
                    break
                
                target_letter = normalized_user_input.lower().strip()[-1]
                
                # Find valid countries that can be chosen next
                valid_countries = [c for c in unused_countries if c.lower().strip().startswith(target_letter)]
                
                # If there are no valid countries to choose from, the game ends
                if not valid_countries:
                    print(f"No valid country found starting with '{target_letter}'. You lose!")
                    break

                new_Current_country = random.choice(valid_countries)
                Current_country = new_Current_country
                print("The next country is:", Current_country)
            else:
                print(
                    f"The country {normalized_user_input} does not start with the last letter of {Current_country}"
                )

    elif choice == "2":
        print("""               Antakshri is a simple word game where players take turns naming countries.
               The first player starts with any country name, and each next player must say a country that begins
               with the last letter of the previous one. For example, if someone says “India,” the next player must
               choose a country starting with “A,” like “Argentina.” Players are usually given a short time limit 
               (around 10–15 seconds) to respond, and no country can be repeated. If a player cannot think of a valid 
               country in time, they are out, and the game continues until only one player remains, who is declared 
               the winner
""")

    elif choice == "3":
        print("Exiting the game. Goodbye!")
        running = False