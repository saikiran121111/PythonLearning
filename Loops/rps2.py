import random
import sys

from enum import Enum

class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

playagain = True

while playagain:

    userinput = input(
    '''
    Choose your choice 
    1.Rock
    2.Paper
    3.Scissors
    end To End this game
    Terminal will terminate the program on wrong option
    ''')

    pythoninput = random.choice('123')

    userChoice = int(userinput)
    pythonChoice = int(pythoninput)

    print('You Choose '+str(RPS(userChoice)).replace('RPS.', ''))
    print('Python Choose '+str(RPS(pythonChoice)).replace('RPS.', ''))

    if userChoice < 1 or userChoice > 3:
        sys.exit('Give proper input man !')

    elif userChoice == pythonChoice :
        print('It\'s a Tie 😁')

    elif userChoice == 1 and pythonChoice == 2:
        print('You loose 🤣')

    elif userChoice == 2 and pythonChoice == 3:
        print('You loose 🤣')

    elif userChoice == 3 and pythonChoice == 1:
        print('You loose 🤣')
    else:
        print('You win 😒')

    playagain = input('Do you want to play again?(y/n)')
    if playagain.lower() == 'y':
        continue # playagain = True also works
    else:
        print('Thank you for playing!!!')
        playagain = False # Break also works
