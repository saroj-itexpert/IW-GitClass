#This program is a prototype for Hangman
import random

words = ["aardvark", "baboon", "camel", "butterfly", "stone", "window"]

chosen_word = random.choice(words)
print(f"Shh the chosen word is: {chosen_word}")

guess = input("Guess a letter: ").lower()

word = []
for letter in chosen_word:
    word.append("_")
