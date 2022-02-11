import os
import CardLib

WhichGame = input('BlackJack or Three Card Poker')
if WhichGame in ['Three Card Poker', 'Poker', 'Three Card', 'poker', 'three card poker', 'three card']:
  InGame = True
  points = 0
  pastpoints = []
  while InGame:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You Have', points)
    points += CardLib.PlayThreeCard()
    pastpoints.append(points)
    if input('Do You Want to Continue?') == 'No':
      InGame = False
elif WhichGame in ['BlackJack','blackjack','Black Jack','black jack']:
  InGame = True
  points = 0
  while InGame:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('You Have', points)
    points += CardLib.PlayBlackJack()
    if input('Do You Want to Continue?') == 'No':
      InGame = False
