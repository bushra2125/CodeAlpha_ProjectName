import random

word_list = ["apple", "table", "water", "stone", "magic"]
chosen_word = random.choice(word_list)

word_display = ['_'] * len(chosen_word)
guessed_letters = []
tries = 6

print("Welcome to Hangman!")
while tries > 0 and '_' in word_display:
    print("\nWord: " + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                word_display[i] = guess
    else:
        tries -= 1
        print(f"Wrong guess! Tries left: {tries}")

if '_' not in word_display:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame Over! The word was:", chosen_word)
