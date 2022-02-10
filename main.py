from random import choice
import os
import matplotlib.pyplot as plt
import CardLib

InGame = True
points = 0
pastpoints = []
for i in range(0,2500):
  os.system('cls' if os.name == 'nt' else 'clear')
  print('You Have', points)
  points += CardLib.PlayThreeCard()
  pastpoints.append(points)
  if points < -10:
    print('You made it', i)
    break
# if input('Do You Want to Continue?') == 'No':
#   InGame = False

plt.plot(pastpoints)
#print(pastpoints)
plt.ylabel('Point Values')
plt.xlabel('Game Number')
plt.figure(figsize=(10, 10))
plt.show()

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