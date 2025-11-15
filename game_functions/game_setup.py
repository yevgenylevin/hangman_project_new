# ========================================
# HANGMAN GAME - SETUP FUNCTIONS
# ========================================
import random

# --- FUNCTION 1 ---
# Write a function that returns a random word from a given word list.
# The function receives a list of words and returns one random word.

def choose_random_word(word_list):
    # OPTION 1 (simplest & best)
    return random.choice(word_list)

    # OPTION 2 (manual index selection)
    # index = random.randrange(len(word_list))
    # return word_list[index]


# --- FUNCTION 2 ---
# Write a function that gets a word, and returns a set of all the unique letters in that word.
# (make sure to lowercase all letters in the word, and dont add white spaces!)

def initialize_letters_to_be_guessed(word):
    letters_set = set()
    for letter in word:
        if letter.isalpha():  # ignore spaces, punctuation, etc.
            letters_set.add(letter.lower())
    return letters_set


# --- FUNCTION 3 ---
# Write a function that returns the alphabet as a list/tuple.
# Input: "abcde" → Output: ["a", "b", "c", "d", "e"]

def initialize_alphabet_display(alphabet: str):
    return list(alphabet)  # simplest correct implementation


# Test your functions here!
if __name__ == "__main__":
    
    ### --- Test Function 1: choose_random_word --- ###
    
    ###Test 1.1###
    # test_words = ["python", "hangman", "programming"]
    # result = choose_random_word(test_words)
    # print(result in test_words)  # Expected: True
    
    ###Test 1.2###
    # test_words = ["apple", "banana", "cherry", "date"]
    # result = choose_random_word(test_words)
    # print(result in test_words)  # Expected: True
    
    ###Test 1.3 - Single word list###
    # test_words = ["onlyword"]
    # result = choose_random_word(test_words)
    # print(result)  # Expected: "onlyword"
    
    
    ### --- Test Function 2: initialize_letters_to_be_guessed --- ###
    
    ###Test 2.1###
    # result = initialize_letters_to_be_guessed("cat")
    # print(result)  # Expected: {"c", "a", "t"}
    
    ###Test 2.2###
    # result = initialize_letters_to_be_guessed("python")
    # print(result)  # Expected: {"p", "y", "t", "h", "o", "n"}
    
    ###Test 2.3###
    # result = initialize_letters_to_be_guessed("banana")
    # print(result)  # Expected: {"b", "a", "n"}
    
    ###Test 2.4###
    # result = initialize_letters_to_be_guessed("Armageddon")
    # print(result)  # Expected: {"a", "r", "m", "g", "e", "d", "o", "n"}
    
    ###Test 2.5###
    # result = initialize_letters_to_be_guessed("Ice Cream")
    # print(result)  # Expected: {"i", "c", "e", "r", "a", "m"}
    
    
    ### --- Test Function 3: initialize_alphabet_display --- ###
    
    ###Test 3.1 - English alphabet###
    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # result = initialize_alphabet_display(alphabet)
    # print(result)
    
    ###Test 3.2 - Short alphabet###
    # alphabet = "abcdefg"
    # result = initialize_alphabet_display(alphabet)
    # print(result)
    
    ###Test 3.3 - Hebrew alphabet###
    # alphabet = "אבגדהוזחטי"
    # result = initialize_alphabet_display(alphabet)
    # print(result)
    
    ###Test 3.4 - Check return type###
    # alphabet = "abc"
    # result = initialize_alphabet_display(alphabet)
    # print(type(result))  # Expected: <class 'list'>
    
    pass
