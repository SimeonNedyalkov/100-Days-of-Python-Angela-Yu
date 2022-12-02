import random

number_of_guesses = 0
from art import logo

print(logo)


def game():
    game_over = False
    easy_mode = 10
    hard_mode = 5
    print("Welcome to the Number Guessing Game! ")
    print("I'm thinking of a number from 1 to 100")
    number = random.randint(1, 100)
    difficulty = input("Choose a difficulty level. Type 'easy' for easy and 'hard' for hard: ")
    if difficulty == "easy":
        number_of_guesses = easy_mode
    elif difficulty == "hard":
        number_of_guesses = hard_mode

    print(f"Psss the number is {number}")
    while not game_over:
        guess = int(input("Make a guess from 1 to 100: "))
        if number_of_guesses == 0:
            game_over = True
            print("Game over!!! ")
        elif guess == number:
            game_over = True
            print(f"You win!!! The actual number was {number} ")
        elif guess > number:
            number_of_guesses -= 1
            game_over = False
            print(number_of_guesses)
            print("Too high!!! ")
        elif guess < number:
            number_of_guesses -= 1
            game_over = False
            print(number_of_guesses)
            print("Too low!!! ")


game()


