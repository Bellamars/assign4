import random

# Uppercase words make comparisons consistent.
# Each word has five letters and no repeated letters.
word_list = ["WALTZ", "GHOST", "LIGHT", "SMILE", "BLUSH"]


def choose_word():
    """Choose and return a random secret word."""
    return random.choice(word_list)


def get_guess(previous_guesses):
    """Ask until the player enters a valid, unused five-letter guess."""
    while True:
        guess = input("Enter a five-letter word: ").strip().upper()

        if len(guess) != 5 or not guess.isalpha():
            print("Please enter exactly five letters.")
        elif guess in previous_guesses:
            print("You already guessed that word. Try another.")
        else:
            return guess


def evaluate_guess(guess, secret_word):
    """Return feedback for each letter: G, Y, or -."""
    feedback = []

    for position in range(5):
        if guess[position] == secret_word[position]:
            feedback.append("G")
        elif guess[position] in secret_word:
            feedback.append("Y")
        else:
            feedback.append("-")

    return feedback


def display_guess(guess, feedback):
    """Print the guess and its feedback."""
    print("Guess:    " + " ".join(guess))
    print("Feedback: " + " ".join(feedback))


def has_won(guess, secret_word):
    """Return True if the guess matches the secret word."""
    return guess == secret_word