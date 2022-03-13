import random
from Words import words

def get_words(words):
    secret_word = random.choice(words)

    return secret_word.upper()


def game():
    secret_word = get_words(words)
    guesses = ""
    tries = 6
    while tries > 0:
        failed = 0
        for letter in secret_word:
            if letter in guesses:
                print(letter)
            else:
                print("_")
                failed += 1
        
        if failed == 0:
            print("you won")
            break

        guess = input("guess a letter: ")
        guesses += guess

        if guess not in secret_word:
            tries -= 1
            print("wrong")
            print(f"you have {tries} turns left")

        if tries == 0:
            print("you lose")


game()