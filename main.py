from wordle_functions import (
    choose_word,
    get_guess,
    evaluate_guess,
    display_guess,
    has_won,
)

print("Welcome to Mystery Wordle!")

play_again = "yes"

while play_again == "yes" or play_again == "y":
    secret_word = choose_word()
    previous_guesses = []
    won = False

    print("\nGuess the five-letter word.")
    print("G = correct letter and position")
    print("Y = correct letter, wrong position")
    print("- = letter is not in the word")

    for attempt in range(1, 7):
        print(f"\nAttempt {attempt} of 6")

        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)

        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)

        if has_won(guess, secret_word):
            print("Congratulations! You solved the puzzle.")
            won = True
            break

    if not won:
        print(f"You used all six attempts. The word was {secret_word}.")

    play_again = input("Would you like to play again? (yes/no): ").strip().lower()

print("Thanks for playing!")