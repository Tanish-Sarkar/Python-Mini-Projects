import random

easy_words = ["apple", "train", "tiger", "money", "india"] 
medium_words = ["python", "bottle", "monkey", "planet", "laptop"] 
hard_words = ["elephant", "diamond", "umbrella", "computer", "mountain"] 

print("Welcome to the Password Guessing Game =>>")
print("Choose your Difficulty level(easy, medium, hard) =>>")

level = input("Enter your difficulty level: ").lower()
if level == "easy":
    secret = random.choice(easy_words)
elif level == "medium":
    secret = random.choice(medium_words)
elif level == "hard":
    secret = random.choice(hard_words)
else:
    print("Invalid Input, Defaulting to easy level...")
    secret = random.choice(easy_words)


attempts = 0
print("\nGussing Games Starts =>>")

while True:
    guess = input("Enter your Guess: ").lower()
    attempts += 1

    if guess == secret:
        print(f"Congrats! you guessed the password in {attempts} attempts.")
        break

    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print(f"Hint: {hint}")

print("Game Over")
    
