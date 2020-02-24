import sys
import random
num = random.randint(1, 10)
money = 100

#Write your game of chance functions here
def coinflip(bet, guess):
  global money
  num = random.randint(1, 2)
  if bet > money:
    print("You do not have enough money.")
  if bet < 0:
    print("You can not bet a negative amount")
  if guess != "Heads" and guess != "Tails":
    print("Please enter guess exactly as Heads or Tails")
  elif num == 1:
    flip = "Heads"
  elif num == 2:
    flip = "Tails"
  elif guess == flip:
    money += bet
    print("You win $" + str(bet) + " Your new total is $" + str(money))
    return money
  elif guess != flip:
    money -= bet
    print("You lose $" + str(bet) + " Your new total is $" + str(money))
    return money

def chohan(guess, bet):
  num1 = random.randint(1, 6)
  num2 = random.randint(1, 6)
  global money
  if (num1 + num2) % 2 == 0:
    dice = "Even"
  elif (num1 + num2) % 2 != 0:
    dice = "Odd"
  if guess == dice:
    money += bet
    print("You guessed correct! Win $" + str(bet) + " Your new total is $" + str(money))
    return money
  elif guess != dice:
    money -= bet
    print("You lose $" + str(bet) + " New total is $" + str(money))
    return money
  
def cardgame(bet):
  global money
  usedcards = []
  card1 = random.randint(1, 13)
  card2 = random.randint(1, 13)
  usedcards.append(card1)
  usedcards.append(card2)
  print (usedcards)
  if card1 > card2:
    money += bet
    print("You win $" + str(bet) + " has been added to wallet. Total is $" + str(money))
  elif card1 < card2:
    money -= bet
    print("You lose $" + str(bet) + " has been removed from wallet. Total is $" + str(money))
  elif card1==card2:
    print("It is a tie, play again")
  return money

def roulette(guess, bet):
  global money
  roll = random.randint(1, 38)
  print(roll)
  if guess == "0" and roll == 37:
    money += bet * 35
    print("You Win $" + str(bet*35) + " New Total is $" + str(money))
  elif guess == "00" and roll == 38:
    money += bet * 35
    print ("You win $" + str(bet*35) + " New Total is $" + str(money))
  elif guess == roll:
    money += bet *35
    print("You win $" + str(bet*35) + " New total is $" + str(money))
  elif guess == "Even" and roll % 2 == 0 and roll!= 37 and roll != 38:
    money += bet
    print("You win $" + str(bet) + " New total is $" + str(money))
  elif guess == "Odd" and roll % 2 != 0 and roll!= 37 and roll != 38:
    money += bet
    print("You win $" + str(bet) + " New total is $" + str(money))
  else:
    money -= bet
    print("You lose $" + str(bet) + " New total is $" + str(money))
    

  
coinflip(2, "Tails")
coinflip(2, "Tails")
chohan("Odd", 15)
cardgame(10)
roulette(8, 15)