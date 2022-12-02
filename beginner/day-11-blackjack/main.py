############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.
import os
# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt
def blackjack():
    game_over = False
    import random
    """Deals a random card"""

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "Its a draw!!!"
        elif computer_score == 0:
            return "You lose!!! "
        elif user_score == 0:
            return "You win!!! "
        elif user_score > 21:
            return "You lose!!! "
        elif computer_score > 21:
            return "You win!!! "
        elif user_score > computer_score:
            return "You win!!! "
        elif computer_score > user_score:
            return "You lose!!! "

    """Calculates the total score"""

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards are: {user_cards} and total score is: {user_score}")
        print(f"Computer's first card is: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            ask = input("Do you want another card ? Type 'y' for yes 'n' for no: ")
            if ask == "y":
                user_cards.append(deal_card())
            elif ask == "n":
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards} and your total score is {user_score}")
    print(f"Computers final hand is {computer_cards} and his total score is {computer_score}")

    print(compare(user_score, computer_score))

    restart = input("Do you want to restart the game? Type 'y' for yes and 'n' for no: ")
    if restart == "y":
        os.system('clear')
        blackjack()
    else:
        game_over == True


blackjack()
