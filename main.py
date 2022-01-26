from random import choice
import os

class deck():

  def __init__(self):
    #Deck Maker
    suits = ['♣','♦','♥','♠']
    cards = ['A','2','3','4','5','6','7','8','9','0','J','Q','K']
    FullDeck = []
    for card in cards:
      for suit in suits:
        FullDeck.append(card + suit)

    self.cards = []
    #Deck Shuffler
    for card in range(0,52):
      RandomCard = choice(FullDeck)
      self.cards.append(RandomCard)
      FullDeck.remove(RandomCard)

  def draw(self, hand):
    hand.append(self.cards.pop())


class hand():
  def __init__(self):
    self.cards = []

  def append(self, item):
    self.cards.append(item)

  def count(self):
    """Returns a tuple (IsBusted, HandValue, HasAces)"""
    HandValue = 0
    AcesCount = 0
    for card in self.cards:
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
      return((False, HandValue, True))
    return((False, HandValue, False))
  
  def PokerCount(self):
    suits = []
    numbers = []
    HandValue = 0
    for card in self.cards:
      if card[0] == 'J':
        numbers.append(11)
      elif card[0] == 'Q':
        numbers.append(12)
      elif card[0] == 'K':
        numbers.append(13)
      elif card[0] == 'A':
        numbers.append(14)
      else:  
        numbers.append(int(card[0]))
      suits.append(card[1])
    numbers.sort()
    UniqueCards = set(numbers)
    if len(UniqueCards) == 1:
      HandValue += 40000
      HandValue += UniqueCards.pop() * 100
    elif len(UniqueCards) == 2:
      HandValue += 10000
      HandValue += numbers[1] * 100
    elif numbers[2] == numbers[1] + 1 and numbers[2] == numbers[0] + 2:
      if len(set(suits)) == 1:
        HandValue += 50000
        HandValue += numbers[2] * 100
      else:
        HandValue += 30000
        HandValue += numbers[2] * 100
    elif len(set(suits)) == 1:
      HandValue += 20000
    HandValue += numbers[2]
    return(HandValue)
    


def PlayBlackJack():

  ShuffledDeck = deck()
  DealerHand = hand()
  YourHand = hand()
  ShuffledDeck.draw(DealerHand)
  ShuffledDeck.draw(YourHand)
  ShuffledDeck.draw(DealerHand)
  ShuffledDeck.draw(YourHand)
  print('Dealers Open Card is', DealerHand.cards[0])
  print('Your Hand is', YourHand.cards)
  if YourHand.count()[2] == True:
    print('Your Count Is',YourHand.count()[1],'/',YourHand.count()[1] - 10)
  else:
    print('Your Count Is',YourHand.count()[1])
  playing = True

  if YourHand.count()[1] == 21:
    print('You Have a Natural')
    print('Dealer Has', DealerHand.cards)
    if DealerHand.count()[1] == 21:
      print('Dealer Also Has a Natural, You Tie')
      return(0)
    else:
      print('Dealer Does Not Have a Natural, You Win')
      return(1.5)
  
  if DealerHand.count()[1] == 21:
    print("Dealer Has BlackJack, You Lose")
    return(-1)

  rounds = 1
  OnFirstHand = False

  if YourHand.cards[0][0] == YourHand.cards[1][0]:
    if input('Do You Want to Split?') == 'yes':
      OnFirstHand = True
      rounds = 2
      SecondHand = hand()
      SecondHand.cards.insert(0,YourHand.cards[1])
      del(YourHand.cards[1])
      ShuffledDeck.draw(YourHand)
      ShuffledDeck.draw(SecondHand)
      print('Your First Hand is', YourHand.cards)
      print('Your Second Hand is', SecondHand.cards)

  TruePointChange = 0
  for round in range(0,rounds):
    answer = input('Double Down?')
    DoubledDown = False
    if answer == 'Yes' or answer == 'yes':
      DoubledDown = True
      ShuffledDeck.draw(YourHand)
      print('Your New Hand is', YourHand.cards)
      playing = False


    while playing:
      HitOrStand = input("Hit or Stand?")
      if HitOrStand == 'Hit':
        ShuffledDeck.draw(YourHand)
        print('Your New Hand is', YourHand.cards)
      elif HitOrStand == 'Stand':
        playing = False
      else:
        print('Thats not a valid command')
      if YourHand.count()[0] == True:
        playing = False
      if YourHand.count()[2] == True:
        print('Your Count Is',YourHand.count()[1],'/',YourHand.count()[1] - 10)
      else:
        print('Your Count Is',YourHand.count()[1])
      print('')
    while DealerHand.count()[1] < 17:
      ShuffledDeck.draw(DealerHand)
      print('Dealers New Hand is', DealerHand.cards)
    print('Dealers Has', DealerHand.cards)
    print('You Have', YourHand.cards)
    if YourHand.count()[0] == True:
      print('Bust, You Lose')
      PointChange = -1
    elif DealerHand.count()[0] == True:
      print('Dealer Busts, You Win')
      PointChange = 1
    elif DealerHand.count()[1] > YourHand.count()[1]:
      print('Dealer has Higher Count, You Lose')
      PointChange =  -1
    elif DealerHand.count()[1] < YourHand.count()[1]:
      print('You Have Higher Count, You Win')
      PointChange = 1
    elif DealerHand.count()[1] == YourHand.count()[1]:
      print('Push, You Tie')
      PointChange = 0
    if DoubledDown:
      PointChange = PointChange * 2
    if OnFirstHand:
      YourHand.cards = SecondHand.cards
      OnFirstHand = False
      print('You Are Now On Your Second Hand')
      print('')
      playing = True
    TruePointChange += PointChange  
  return(TruePointChange)

def PlayThreeCard():
  ShuffledDeck = deck()
  YourHand = hand()
  DealerHand = hand()
  for card in range(0,3):
    ShuffledDeck.draw(YourHand)
    ShuffledDeck.draw(DealerHand)
  print(YourHand.cards)
  Raised = input("Raise or Fold?")
  if Raised == "Raise" or Raised == "raise":
    print(YourHand.PokerCount())
    print(DealerHand.cards)
    print(DealerHand.PokerCount())
    if DealerHand.PokerCount() <= YourHand.PokerCount():
      print('You Win')
      return(1)
    else:
      print('You Lose')
      return(-1)
  else:
    return(-0.5)

InGame = True
points = 0
while InGame:
  os.system('cls' if os.name == 'nt' else 'clear')
  print('You Have', points)
  points += PlayThreeCard()
  if input('Do You Want to Continue?') == 'No':
    InGame = False


'''
InGame = True
points = 0
while InGame:
  os.system('cls' if os.name == 'nt' else 'clear')
  print('You Have', points)
  points += PlayBlackJack()
  if input('Do You Want to Continue?') == 'No':
    InGame = False
'''