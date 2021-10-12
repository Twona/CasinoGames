import random
from random import randrange
import time

playGame = True
Money = 1000


# Function to draw one random card
class drawCard():
    def __init__(self, cardDrawValue, cardName, cardDrawSuit):
        self.cardDrawValue = randrange(1, 14)
        self.cardSuits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cardDrawSuit = random.sample(self.cardSuits, 4)
        self.cardName = cardDrawValue

    def drawthecard(self, cardDrawValue, cardName, cardDrawSuit):
        cardDrawValue = randrange(1, 14)
        cardSuits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        cardDrawSuit = random.sample(cardSuits, 4)
        cardName = cardDrawValue
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
        return self.cardDrawValue, self.cardName, self.cardDrawSuit


def gameBegin(Money):
    while playGame:
        print("You have $" + str(Money) + ". Each play is $5.")
        time.sleep(1)

        # Set default values for both cards
        cardDrawValue1 = 0
        cardName1 = ""
        cardDrawSuit1 = ""
        cardDrawValue2 = 0
        cardName2 = ""
        cardDrawSuit2 = ""

        # Draw card and present it to player
        drawCard(cardDrawValue1, cardName1, cardDrawSuit1)
        print("Your first card is a " + cardName1 + " of " + cardDrawSuit1 + ".")

        # Let player guess with loop to check input
        input("Will you guess High (1) or Low(2):")
        while input != 1 or input != 2:
            input("Invalid entry. Please enter 1 for High or 2 for Low:")

        # Draw second card and present it to player
        drawCard(cardDrawValue2, cardName2, cardDrawSuit2)
        print("your second card is a " + cardName2 + " of " + cardDrawSuit2 + ".")
        time.sleep(1)

        # Logic to check card value and if player won or lost
        if input == 1:
            if cardDrawValue1 > cardDrawValue2:
                Money += 5
                print("You have won $5!")
            elif cardDrawValue1 < cardDrawValue2:
                Money -= 5
                print("You lost $5.")
            else:
                print("It's a tie. Your money will be returned.")
        elif input == 2:
            if cardDrawValue1 > cardDrawValue2:
                Money -= 5
                print("You lost $5.")
            elif cardDrawVale1 < cardDrawValue2:
                Money += 5
                print("You have won $5.")
            else:
                print("It's a tie. Your money will be returned.")


gameBegin(Money)

