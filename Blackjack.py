
import random
def main():
  print('***********************************')
  print('** Welcome to BlackJack! **')
  print('***********************************')



  player()
  dealer()

def hit():
  first = random.randint(1,13)
  if first == 11 or first == 12 or first == 13:
    first = 10
  return first

def player():
  player_hand = hit()
  print('Your first card is: %d' % player_hand)
  
  print()
  answer = 'y'
  while player_hand < 21 and answer == 'y':
   print('Do you want another card?')
   answer = input('Type y for Yes, n for No: ')
   print()
   if answer == 'y':
     draw = random.randint(1,13)
     if draw == 11 or draw == 12 or draw == 13:
       draw = 10
     player_hand = player_hand + draw
     print('Your next card is: %d' % draw)
     print('Your combined value is %d' % player_hand)
     print()
   if answer == 'n':
     player_hand = player_hand
     print('Your combined value is %d' % player_hand)
     break
   if player_hand > 21:
     print('Bust')
     break
   if player_hand == 21:
     print('21!')
     break
  return player_hand

def dealer():
  dealer_hand = 0
  if dealer_hand < 17:
    while dealer_hand < 17:
      print('Dealer draws another card.')
      dealer_hand = hit()
      print('Dealer\'s card is: %d' % dealer_hand)
      dealer_hand = dealer_hand + hit()
      print('Dealer\'s value is %d, you have %d' % (dealer_hand,dealer_hand)) #how to get player_hand here
  if dealer_hand >= 17:
    print('Stand')
  return dealer_hand
main()
