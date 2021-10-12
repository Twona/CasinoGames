import random
from random import randrange
import time

playGame = True
Money = 1000


# Function to draw one random card
class drawCard:
    cardDrawValue = randrange(1, 14)
    cardSuits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    cardDrawSuit = random.sample(cardSuits, 1)
    cardName = cardDrawValue

    # Changes card name if face card
    if cardDrawValue == 1:
        cardName = "Ace"
    elif cardDrawValue == 11:
        cardName = "Jack"
    elif cardDrawValue == 12:
        cardName = "Queen"
    elif cardDrawValue == 13:
        cardName = "King"
    else:
        cardName = str(cardDrawValue)


def gameBegin(Money):
    while playGame:
        print("You have $" + str(Money) + ". Each play is $5.")
        time.sleep(1)

        # Set default values for both cards
        # cardOne = drawCard
        # cardTwo = drawCard

        # Draw card and present it to player
        print(f"Your first card is a", cardOne.cardName, "of", str(cardOne.cardDrawSuit), ".")

        # Let player guess with loop to check input
        choice = input("Will you guess High (1) or Low (2):")
        while choice not in ["1", "2"]:
            choice = input("Invalid choice. Please guess High (1) or Low (2):")

        # Draw second card and present it to player
        print(f"Your second card is a", cardTwo.cardName, "of", str(cardTwo.cardDrawSuit), ".")
        time.sleep(1)

        # Logic to check card value and if player won or lost
        if input == "1":
            if cardOne.cardDrawValue > cardTwo.cardDrawValue:
                Money += 5
                print("You have won $5!")
            elif cardOne.cardDrawValue < cardTwo.cardDrawValue:
                Money -= 5
                print("You lost $5.")
            else:
                print("It's a tie. Your money will be returned.")
        elif input == "2":
            if cardOne.cardDrawValue > cardTwo.cardDrawValue:
                Money -= 5
                print("You lost $5.")
            elif cardOne.cardDrawVale < cardTwo.cardDrawValue2:
                Money += 5
                print("You have won $5.")
            else:
                print("It's a tie. Your money will be returned.")


gameBegin(Money)

