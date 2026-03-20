import sys
import random
from enum import Enum

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

playerOption = input('Choose\n 1.Rock\n 2.Paper\n 3.Scissors\n')

playerChoice = int(playerOption)

if playerChoice < 1 or playerChoice > 3:
    sys.exit('Invalid option Please choose between 1 and 3')

pythonOption = random.choice(('1', '2', '3'))
pythonChoice = int(pythonOption)

print('You chose: '+ str(RPS(playerChoice)).replace('RPS.',''))
print('Python chose: '+ str(RPS(pythonChoice)).replace('RPS.',''))

if pythonChoice == playerChoice:
    print('Tie')

elif pythonChoice == 1 and playerChoice == 2:
    print('You win')
elif pythonChoice == 2 and playerChoice == 3:
    print('You win')
elif pythonChoice == 3 and playerChoice == 1:
    print('You win')
else:
    print('You loose')