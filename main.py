import random
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
print(f"{logo}")
#Testing code
print(f'Pssst, the solution is {chosen_word}.')


display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"

end_of_game = False

lives = 6

# Game loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Check for already guessed letter
    if guess in display:
      print(f"You've already guessed {guess}! Try another letter.")
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    # Decrease lives count if letter does not exist, also check to see if count is 0 to print Game Over
    if guess not in chosen_word:
      lives -= 1
      print(f"{stages[lives]}")
      print(f"The letter {guess} is not in the word. Try again.")
      if lives == 0:
        end_of_game = True
        print("Game Over!")
    # Display progress of word guessed
    print(f"{' '.join(display)}")
    # Win screen
    if "_" not in display:
        end_of_game = True
        print(f"The word was {''.join(display)}!")
        print("You've won!")
        
