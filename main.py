import random

def choose_difficulty():

    print("\nChoose a difficulty level: ")
    print("1 - Easy (1-50)")
    print("2 - Medium (1-100)")
    print("3 - Hard (1-1000)")


    while True:
        choice = input("Your choice (1/2/3): ")
        if choice == "1":
            return 1, 50
    
        elif choice == "2":
            return 1, 100
    
        elif choice == "3":
            return 1, 1000
    
        else:
            print("Choice please 1, 2 or 3")

def play_game():
    low, high = choose_difficulty()
    secret_number = random.randint(low, high)
    attempts = 0

    print(f"\nI thought of a number between {low} and {high}. Guess it!")
    

    while True:
        guess = input("Try to guess the number: ")

        if not guess.isdigit():
            print("Please enter only numbers!")
            continue

        guess = int(guess)
        attempts += 1 

        if guess < secret_number:
            print("My number is higher.")

        elif guess > secret_number:
            print("My number is lower.")
    
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            return attempts
        
def main():
        best_core = None

        while True:
            attempts = play_game()

            if best_core is None or attempts < best_core:
                best_core = attempts
                print(f"New record: {best_core} attempts")
            else:
                print(f"Your current record: {best_core} attempts")


            again = input("\nWant to play again? (yes/no): ").lower()
            if again not in ("yes", "y"):
                print("See you later! Thanks for playing")
                break


if __name__ == "__main__":
    main()

