
import random

WORDS = [
    "python",
    "laptop",
    "coding",
    "computer",
    "developer",
    "programming",
    "keyboard"
]


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    attempts = 6

    print("\n================================")
    print("       WELCOME TO HANGMAN")
    print("================================")
    print("Guess the hidden word one letter at a time!")
    print("You have", attempts, "wrong attempts available.")

    while attempts > 0:
        display = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("\nWord:", display)
        print("Wrong attempts left:", attempts)
        print(
            "Guessed letters:",
            ", ".join(sorted(guessed_letters)) or "None"
        )

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word!")
            print("The word was:", secret_word)
            return

        guess = input("\nEnter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

    print("\nGAME OVER!")
    print("The correct word was:", secret_word)


def main():
    while True:
        play_hangman()

        while True:
            choice = input("\nPlay again? (yes/no): ").strip().lower()

            if choice in ("yes", "y"):
                break
            elif choice in ("no", "n"):
                print("\nThanks for playing Hangman!")
                print("Goodbye!")
                return
            else:
                print("Please enter yes or no.")


if __name__ == "__main__":
    main()
