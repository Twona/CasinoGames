import random
from random import randrange
import time
import os

playGame = True
payout = False
money = 1000
bet = 1
jackpot = 0

#Create and Format the Display
class slotDisplay:
  symbols = ["Peach", "Apple", "Cherries", "Orange", "King", "Bar", "Seven", "Triple Sevens", "?"]

  def __init__(self):
    self.reel1 = []
    self.reel2 = []
    self.reel3 = []

  def spinSlot(self):
    reel1 = []
    reel2 = []
    reel3 = []
    while len(reel1) and len(reel2) and len(reel3) < 3:
      x = randrange(1,len(symbols)+1)
      y = randrange(1,len(symbols)+1)
      z = randrange(1,len(symbols)+1)
      reel1.append = symbols[x]
      reel2.append = symbols[y]
      reel3.append = symbols[z]

    return reel1, reel2, reel3

def gameBegin(Money):
  while playGame:

    # Initialize Machine
    var = []
    slotmachine = slotDisplay
    slotmachine = slotDisplay.spinSlot(var)
    print("Welcome! Minimum bet is $1")
    time.sleep(0.5)
    print("You have $" + str(Money) + ".")
    time.sleep(1)
    bet = input("What will you bet:")

    # Check that bet is valid
    while bet < "1":
      print("Sorry, that is not a valid bet.")
      bet = input("What will you bet:")
    while isinstance(int(bet), int) == False:
      print("Sorry, that is not a valid bet.")
      bet = input("What will you bet:")

    # Call Jackpot to function and add to Jackpot
    global jackpot
    jackpot += int(bet)

    # Print out slot spin
    print("Slot is spinning...")
    time.sleep(1)
    print(slotmachine.reel1[1], slotmachine.reel2[1], slotmachine.reel3[1])
    print(slotmachine.reel1[2], slotmachine.reel2[2], slotmachine.reel3[2])
    print(slotmachine.reel1[3], slotmachine.reel2[3], slotmachine.reel3[3])

gameBegin(money)
