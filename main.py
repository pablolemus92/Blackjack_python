############### Blackjack Project #####################



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


#1: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
from art import logo
import random
from replit import clear

"""returns a random card"""
def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card

#2: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.
def calculate_score(cards):
  """Take a list of cards and return the score calulated from the cards"""
  
  #3: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of     the actual score. 0 will represent a blackjack in our game.
  if sum(cards) == 21 and len(cards) == 2:
    return 0; 
  #4: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.appened(1)
  return sum(cards)

#5: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif user_score > 21 and computer_score > 21:
    return "You went over, You Lose :("
  elif computer_score == 0:
    return "You Lose :("
  elif user_score == 0: 
    return "You Won!!!"
  elif user_score > 21: 
    return "Computer Won!"
  elif computer_score > 21:
    return "You Won!!!"
  elif user_score > computer_score:
    return "User Won!!!"
  else: 
    return "You Lose :("

def play_game():
  
  print(logo)
  
  #6: Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  is_gameover = False
  
  for _ in range(2):
    user_cards.append(deal_cards())
    computer_cards.append(deal_cards())
    
  #7: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while not is_gameover:
    #8: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21,      then the game ends.
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  your card {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    if user_score == 0  or computer_score == 0 or user_score > 21:
      is_gameover =  True
    else: 
      #9: If the game has not ended, ask the user if they want to draw another card. If yes, then use the                deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      user_cont_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_cont_deal == 'y':
        user_cards.append(deal_cards())
      else:
        is_gameover = True
      
  #10: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while computer_score != 0 and computer_score < 17: 
    computer_cards.append(deal_cards())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand: {user_cards}, final score: {user_score} ")
  print(f"  Computer final hand: {computer_cards}, final score: {computer_score} ")
  print(compare(user_score, computer_score))

#12: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want a game of blackjack the game? Type 'y' for yes or 'n' for no. ") == 'y':
  clear()
  play_game()


