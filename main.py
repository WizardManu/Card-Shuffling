from random import choice
import os
def MakeAndShuffleDeck():
  #Deck Maker
  suits = ['♣','♦','♥','♠']
  cards = ['A','2','3','4','5','6','7','8','9','0','J','Q','K']
  FullDeck = []
  for card in cards:
    for suit in suits:
      FullDeck.append(card + suit)

  ShuffledDeck = []
  #Deck Shuffler
  for card in range(0,52):
    RandomCard = choice(FullDeck)
    ShuffledDeck.append(RandomCard)
    FullDeck.remove(RandomCard)
  return(ShuffledDeck)
#print(ShuffledDeck)

def PlayBlackJack():
  def Count(hand):
    HandValue = 0
    AcesCount = 0
    for card in hand:
      value = card[0]
      if value == '0':
        value = 10
      elif value == 'J' or value == 'Q' or value == 'K':
        value = 10
      elif value == 'A':
        AcesCount += 1
        value = 11
      value = int(value)
      HandValue += value
    while AcesCount > 0 and HandValue > 21:
      HandValue = HandValue - 10
      AcesCount = AcesCount - 1
    if HandValue > 21:
      return((True, HandValue,False))
    if AcesCount > 0:
      return((False,HandValue,True))
    return((False, HandValue,False))

  DealerHand = [ShuffledDeck.pop()]
  YourHand = [ShuffledDeck.pop()]
  DealerHand.append(ShuffledDeck.pop())
  YourHand.append(ShuffledDeck.pop())
  print('Dealers Open Card is', DealerHand[0])
  print('Your Hand is', YourHand)
  if Count(YourHand)[2] == True:
    print('Your Count Is',Count(YourHand)[1],'/',Count(YourHand)[1] - 10)
  else:
    print('Your Count Is',Count(YourHand)[1])
  playing = True

  if Count(YourHand)[1] == 21:
    print('You Have a Natural')
    print('Dealer Has', DealerHand)
    if Count(DealerHand)[1] == 21:
      print('Dealer Also Has a Natural, You Tie')
      return(0)
    else:
      print('Dealer Does Not Have a Natural, You Win')
      return(1.5)
  
  if Count(DealerHand)[1] == 21:
    print("Dealer Has BlackJack, You Lose")
    return(-1)


  answer = input('Double Down?')
  DoubledDown = False
  if answer == 'Yes' or answer == 'yes':
    DoubledDown = True
    YourHand.append(ShuffledDeck.pop())
    print('Your New Hand is', YourHand)
    playing = False


  while playing:
    HitOrStand = input("Hit or Stand?")
    if HitOrStand == 'Hit':
      YourHand.append(ShuffledDeck.pop())
      print('Your New Hand is', YourHand)
    elif HitOrStand == 'Stand':
      playing = False
    else:
      print('Thats not a valid command')
    if Count(YourHand)[0] == True:
      playing = False
    if Count(YourHand)[2] == True:
      print('Your Count Is',Count(YourHand)[1],'/',Count(YourHand)[1] - 10)
    else:
      print('Your Count Is',Count(YourHand)[1])
    print('')
  while Count(DealerHand)[1] < 17:
    DealerHand.append(ShuffledDeck.pop())
    print('Dealers New Hand is', DealerHand)
  print('Dealers Has', DealerHand)
  print('You Have', YourHand)
  if Count(YourHand)[0] == True:
    print('Bust, You Lose')
    PointChange = -1
  elif Count(DealerHand)[0] == True:
    print('Dealer Busts, You Win')
    PointChange = 1
  elif Count(DealerHand)[1] > Count(YourHand)[1]:
    print('Dealer has Higher Count, You Lose')
    PointChange =  -1
  elif Count(DealerHand)[1] < Count(YourHand)[1]:
    print('You Have Higher Count, You Win')
    PointChange = 1
  elif Count(DealerHand)[1] == Count(YourHand)[1]:
    print('Push, You Tie')
    PointChange = 0
  if DoubledDown:
    PointChange = PointChange * 2
  return(PointChange)

InGame = True
points = 0
while InGame:
  ShuffledDeck = MakeAndShuffleDeck()
  os.system('cls' if os.name == 'nt' else 'clear')
  print('You Have', points)
  points += PlayBlackJack()
  if input('Do You Want to Continue?') == 'No':
    InGame = False