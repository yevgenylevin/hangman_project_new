# ========================================
# HANGMAN GAME - INPUT & VALIDATION
# ========================================

# --- FUNCTION 1 ---
# Ask user for input and return it as lowercase.
def get_letter_from_user():
    return input().strip().lower()


# --- FUNCTION 2 ---
# Check if input is a single alphabetical letter.
def is_valid_letter(input_letter):
    return len(input_letter) == 1 and input_letter.isalpha()


# --- FUNCTION 3 ---
# Check if letter was already guessed.
def is_already_guessed(letter, guessed_letters):
    return letter in guessed_letters


# --- FUNCTION 4 ---
# Keep asking until a valid, new letter is entered.
def get_valid_guess(guessed_letters):
    while True:
        user_input = get_letter_from_user()

        # Check validity
        if not is_valid_letter(user_input):
            print("Invalid input. Enter ONE letter (a-z).")
            continue

        # Check if already guessed
        if is_already_guessed(user_input, guessed_letters):
            print("You already guessed that letter. Try another one.")
            continue

        return user_input


# Test your functions here!
if __name__ == "__main__":
    
    ### --- Test Function 1: get_letter_from_user --- ###
    # print("Please enter a letter:")
    # letter = get_letter_from_user()
    # print(f"You entered: {letter}")
    
    
    ### --- Test Function 2: is_valid_letter --- ###
    # result = is_valid_letter("G")
    # print(result)  # Expected: True
    
    # result = is_valid_letter("a")
    # print(result)  # Expected: True
    
    # result = is_valid_letter("tar")
    # print(result)  # Expected: False
    
    # result = is_valid_letter("y-")
    # print(result)  # Expected: False
    
    # result = is_valid_letter("")
    # print(result)  # Expected: False
    
    # result = is_valid_letter("5")
    # print(result)  # Expected: False
    
    # result = is_valid_letter(" ")
    # print(result)  # Expected: False
    
    
    ### --- Test Function 3: is_already_guessed --- ###
    # result = is_already_guessed("a", {"a", "b", "c"})
    # print(result)  # Expected: True
    
    # result = is_already_guessed("d", {"a", "b", "c"})
    # print(result)  # Expected: False
    
    # result = is_already_guessed("x", set())
    # print(result)  # Expected: False
    
    # result = is_already_guessed("b", {"a", "b", "c", "d", "e"})
    # print(result)  # Expected: True
    
    
    ### --- Test Function 4: get_valid_guess --- ###
    # print("Enter a valid letter:")
    # letter = get_valid_guess(set())
    # print(f"Valid letter entered: {letter}")
    
    pass
