import random

# Dictionary mapping the number of incorrect guesses to the corresponding ASCII art
pics = {
    0: """
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    1: """
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    2: """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    3: """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    4: """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    5: """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    6: """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
}

def play_game():
    # Corrected spelling of 'benevolent', preserving all user code logic
    words = ["dosa", "benevolent", "coder", "debug", "array"]
    tword = random.choice(words)
    stat = ["_"] * len(tword)
    max_inc = 6
    wrong = 0
    right = []

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(tword)} letters.")
    
    while wrong < max_inc and "_" in stat:
        # Display the current hangman graphic based on the 'wrong' counter
        print(pics[wrong])
        
        print("\nWord: " + " ".join(stat))
        print(f"Incorrect guesses remaining: {max_inc - wrong}")
        print(f"Letters already guessed: {', '.join(right)}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in right:
            print("You already guessed that letter. Try again.")
            continue
            
        right.append(guess)
        
        if guess in tword:
            print(f"Good job! '{guess}' is in the word.")
            for index, letter in enumerate(tword):
                if letter == guess:
                    stat[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            wrong += 1
            
    print("\n----------------- Game Over ----------------")
    
    # Display the final state of the graphic before announcing the result
    print(pics[wrong])
    
    if "_" not in stat:
        print(f"Congratulations! You guessed the word: {tword}")
    else:
        print(f"You ran out of guesses. The word was: {tword}")

if __name__ == "__main__":
    play_game()
