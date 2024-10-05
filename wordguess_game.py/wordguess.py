import random
import time  # Add this to introduce a small delay

# Ask for the user's name
name = input("What is your name? ")

# Print a message with the user's name
print("Good Luck, ", name )

# Introduce a slight delay before the game starts
time.sleep(1)

# List of words for the game
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Randomly choosing a word from the list
word = random.choice(words)

print("Guess the characters!")

guesses = ''  # Store the guessed characters
turns = 12  # Number of allowed wrong guesses

# Main game loop
while turns > 0:

    failed = 0  # Track unguessed characters

    # Loop through each character in the word
    for char in word:

        if char in guesses:
            print(char, end=" ")  # Show the guessed character
        else:
            print("_", end=" ")  # Show underscore for unguessed character
            failed += 1

    print()  # Print a newline after the word

    # If no unguessed characters, the player wins
    if failed == 0:
        print("You Win!")
        print("The word is:", word)
        break

    # Input for the player's next guess
    guess = input("Guess a character: ")

    # Add the guessed character to the guesses
    guesses += guess

    # If the guessed character is not in the word
    if guess not in word:
        turns -= 1  # Reduce the number of remaining turns
        print("Wrong guess!")
        print("You have", turns, "more guesses.")

        # If no turns are left, the player loses
        if turns == 0:
            print("You Lose. The word was:", word)




# o/p gets in bash  "python wordguess.py"