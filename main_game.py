# ========================================
# HANGMAN GAME - MAIN
# ========================================

from game_functions.game_setup import (
    choose_random_word,
    initialize_letters_to_be_guessed,
    initialize_alphabet_display,
)
from game_functions.game_logic import (
    check_letter_in_word,
    get_hidden_word_with_visible_guessed_letters,
    update_guessed_letters,
    update_letters_to_be_guessed,
)
from game_functions.input_and_validations import get_valid_guess
from game_functions.display_and_feedback import (
    show_hangman,
    display_game_status,
    show_win_message,
    show_lose_message,
)
from game_functions.game_state import (
    check_win_condition,
    check_lose_condition,
    is_game_over,
)
from common.ascii_art import hangman_7_stages


# You can keep this list here or move it into a config file if needed
WORD_LIST = [
    "banana",
    "monkey",
    "zoom",
    "cat",
    "dog",
    "avocado",
    "epic",
    "melon",
    "tomato",
]


def main():
    print("Welcome to the Hangman game!")
    print("-" * 35)

    # 1. Choose secret word
    secret_word = choose_random_word(WORD_LIST).lower()

    # 2. Prepare game state
    hidden_letters = initialize_letters_to_be_guessed(secret_word)
    guessed_letters = set()
    letters_alphabet = initialize_alphabet_display("abcdefghijklmnopqrstuvwxyz")

    max_incorrect_guesses = len(hangman_7_stages) - 1  # e.g. 6 if 0–6 stages
    incorrect_guesses = 0
    attempts_remaining = max_incorrect_guesses

    # 3. Game loop
    while not is_game_over(hidden_letters, attempts_remaining):
        print()
        # Show hangman + status
        print(show_hangman(incorrect_guesses))
        display_game_status(
            letters_alphabet=letters_alphabet,
            guessed_letters=guessed_letters,
            hidden_word=secret_word,
            attempts_remain=attempts_remaining,
        )

        print()  # spacing
        print("Please guess a letter:")
        guess = get_valid_guess(guessed_letters)

        # Add to guessed set
        update_guessed_letters(guess, guessed_letters)

        # Correct / incorrect logic
        if check_letter_in_word(guess, secret_word):
            update_letters_to_be_guessed(hidden_letters, guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            attempts_remaining = max_incorrect_guesses - incorrect_guesses
            print(f"Wrong guess. '{guess}' is not in the word.")

    # 4. Game ended – show final state and message
    print()
    print(show_hangman(incorrect_guesses))

    # Final word display
    final_display = get_hidden_word_with_visible_guessed_letters(
        secret_word, guessed_letters
    )
    print(f"Final word state: {final_display}")

    if check_win_condition(hidden_letters):
        show_win_message(secret_word)
    elif check_lose_condition(attempts_remaining):
        show_lose_message(secret_word)
    else:
        # Should not normally happen, but just in case
        print("Game over – unexpected state.")


if __name__ == "__main__":
    main()
