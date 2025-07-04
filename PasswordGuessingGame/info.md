# 🔐 Password Guessing Game 🧠

-----

Welcome to the **Password Guessing Game**\! This is a fun and simple command-line game where you try to guess a secret word. Test your vocabulary and deduction skills as you receive hints after each incorrect attempt.

-----

## ✨ Features

  * **Difficulty Levels**: Choose from Easy, Medium, or Hard to match your skill level.
  * **Interactive Hints**: After each incorrect guess, receive a hint showing correctly placed letters.
  * **Attempt Counter**: Keep track of how many guesses it takes you to crack the password.
  * **Customizable Word Lists**: Easily add or modify the secret words for endless fun\!

-----

## 🚀 How to Run

1.  **Save the Code**: Ensure the provided Python code is saved in a file named `PasswordGuessingGame.py`.
2.  **Run from Terminal**: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script using:
    ```bash
    python PasswordGuessingGame.py
    ```

-----

## 💡 How to Play

1.  **Choose Difficulty**: When the game starts, you'll be prompted to select a difficulty level: `easy`, `medium`, or `hard`. Type your choice and press Enter. If you enter an invalid choice, the game will default to `easy`.
2.  **Start Guessing**: The game will then begin. You'll be asked to "Enter your Guess:".
3.  **Receive Hints**:
      * If your guess is incorrect, you'll receive a `Hint:`. This hint will show underscores `_` for letters you haven't guessed correctly or haven't placed correctly, and the actual letter for any characters that are in the correct position.
      * For example, if the secret word is `apple` and you guess `apply`, the hint might be `appl_`.
4.  **Keep Guessing**: Continue entering guesses based on the hints until you find the secret word\!
5.  **Victory\!**: Once you guess the correct password, the game will congratulate you and tell you how many attempts it took.

-----

## 🛠️ Customization

Want to make the game even more challenging or add your own themed words? You can easily modify the word lists directly in the `PasswordGuessingGame.py` file:

```python
easy_words = ["apple", "train", "tiger", "money", "india"]
medium_words = ["python", "bottle", "monkey", "planet", "laptop"]
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"]

# Add or remove words from these lists to customize your game!
# Make sure all words are lowercase for consistency.
```

-----