from random import randint

rpsList = ['Rock', 'Paper', 'Scissors']

computer = rpsList[randint(0, 2)]

player = False

while player == False:
  player = input('Rock, Paper, Scissors? ')
  
  if player == computer:
    print('Tie!')
  elif player == 'Rock':
    if computer == 'Paper':
      print('You Lost!', computer, "covers", player)
    else:
      print('You Win!', player, "smashes", computer)
  elif player == 'Paper':
    if computer == 'Scissors':
      print('You Lost!', computer, "cuts", player)
    else:
      print('You Win!', player, "covers", computer)
  elif player == 'Scissors':
    if computer == 'Rock':
      print('You Lost!', computer, "smashes", player)
    else:
      print('You Win!', player, "cuts", computer)
  else:
    print('Please pick a valid input')
  
  computer = rpsList[randint(0, 2)]
  player = False
