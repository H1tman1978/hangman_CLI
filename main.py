# Step 5
import os
import random

from hangman_words import word_list
from hangman_art import logo, stages

# Function to clear the screen
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
letters_guessed = []

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    clearConsole()  # Clear the previous round
    print(logo)
    print(f"{' '.join(display)}")
    print(stages[lives])
    guess = input("Guess a letter: ").lower()

    if guess in letters_guessed:
        print(f"You've already guessed '{guess}'")
        continue
    else:
        letters_guessed.append(guess)

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"'{guess}' is not in the word.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose. The word was {chosen_word}.")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
