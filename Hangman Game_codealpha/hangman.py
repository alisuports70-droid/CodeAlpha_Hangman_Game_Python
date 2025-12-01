import random

# Step 1: Word List
words = ["apple", "tiger", "water", "phone", "chair"]

# Step 2: Random Secret Word
secret_word = random.choice(words)

# Step 3: Display with underscores
display = ['_' for _ in secret_word]

attempts = 0
guessed_letters = set()   # <- NEW FIX

while attempts < 6 and "_" in display:
    
    guess = input("Guess a letter: ").lower()
    
    # 1. Validate guess length (only 1 char allowed)
    if len(guess) != 1:
        print("Please enter a single letter.")
        continue

    # 2. Check repeated guesses (correct/wrong both)
    if guess in guessed_letters:
        print("You already guessed this letter. Try another!")
        continue

    guessed_letters.add(guess)

    # 3. Check if guess is in secret_word
    if guess in secret_word:
        for index in range(len(secret_word)):
            if secret_word[index] == guess:
                display[index] = guess

        print("Correct guess!", " ".join(display))

    else:
        attempts += 1
        attempts_left = 6 - attempts
        print(f"Wrong guess! You have {attempts_left} attempts left.")

# Step 4: Game Over Conditions
if "_" not in display:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Game over! The word was:", secret_word)

print("Thanks for playing Hangman!")
