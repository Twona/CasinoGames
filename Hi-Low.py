import random
from random import randrange
import time
import os

playGame = True
payout = False
Money = 1000


# Function to draw one random card
class drawCard:

    def __init__(self):
        self.cardDrawValue = int()
        self.cardDrawSuit = ""
        self.cardName = ""

class drawPlayerCard(drawCard):
    def genCard(self):
        cardSuits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cardDrawValue = int(randrange(1, 14))
        self.cardDrawSuit = random.sample(cardSuits, 1)
        self.cardName = drawPlayerCard.nameChange(self.cardDrawValue)

        return self

    def nameChange(cardDrawValue):
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

        return cardName

def resetCards(cardOne, cardTwo):
    cardOne = ""
    cardTwo = ""
    return cardOne, cardTwo

def gameBegin(Money):
    while playGame:
        # Initialize cards
        cardOne = ""
        cardTwo = ""
        print("Shuffling cards...")
        time.sleep(1)
        print("You have $" + str(Money) + ". Each play is $5.")
        time.sleep(1)

        # Set default values for both cards
        cardOne = drawCard
        cardOne = drawPlayerCard.genCard(cardOne)
        cardTwo = drawPlayerCard
        cardTwo = drawPlayerCard.genCard(cardTwo)


        # Draw card and present it to player
        print(f"Your first card is a", cardOne.cardName, "of", str(cardOne.cardDrawSuit), ".")

        # Let player guess with loop to check input
        choice = input("Will you guess High (1), Low (2), or Equal(3):")
        while choice not in ["1", "2", "3"]:
            choice = input("Invalid choice. Please guess High (1), Low (2), or Equal(3):")

        # Draw second card and present it to player
        print(f"Your second card is a", cardTwo.cardName, "of", str(cardTwo.cardDrawSuit), ".")
        time.sleep(2)
        payout = True

        # Logic to check card value and if player won or lost
        while payout:
            if choice == "1":
                if cardOne.cardDrawValue < cardTwo.cardDrawValue:
                    Money += 5
                    print("You have won $5!")
                    time.sleep(2)
                    payout = False
                elif cardOne.cardDrawValue > cardTwo.cardDrawValue:
                    Money -= 5
                    print("You lost $5.")
                    time.sleep(2)
                    payout = False
                else:
                    print("It's a tie. Your money will be returned.")
                    time.sleep(2)
                    payout = False
            elif choice == "2":
                if cardOne.cardDrawValue < cardTwo.cardDrawValue:
                    Money -= 5
                    print("You lost $5.")
                    time.sleep(2)
                    payout = False
                elif cardOne.cardDrawValue > cardTwo.cardDrawValue:
                    Money += 5
                    print("You have won $5.")
                    time.sleep(2)
                    payout = False
                else:
                    print("It's a tie. Your money will be returned.")
                    time.sleep(2)
                    payout = False
            elif choice == "3":
                if cardOne.cardDrawValue != cardTwo.cardDrawValue:
                    Money -= 5
                    print("You lost $5.")
                    time.sleep(2)
                    payout = False
                else:
                    Money += 100
                    print("Good guess! You won $100!")
                    time.sleep(2)
                    payout = False

        resetCards(cardOne, cardTwo)
        os.system('cls||clear')  # Clear Screen


gameBegin(Money)
