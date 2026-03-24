import random
from enum import Enum


def rps():

    class stats(Enum):
        Rock = 1
        Paper = 2
        Scissors = 3

    user_input = int(input(
        '''
        Enter your choice:
        1.Rock
        2.Paper
        3.Scissors
        '''))

    python_input = int(random.choice('123'))

    if user_input in (1,2,3):
        print('You choose' +' '+ str(stats(user_input)).replace('stats.',''))
        print('Python choose'+' '+str(stats(python_input)).replace('stats.',''))

    if user_input not in (1, 2, 3) :
        print('The provided option is not valid')
        return rps() # recursion so it will start the game

    elif(user_input == python_input):
        print('Tie!')
    elif user_input == 1 and python_input == 2:
        print('You loose!')
    elif user_input == 2 and python_input == 3:
        print('You loose!')
    elif user_input == 3 and python_input == 1:
        print('You loose!')
    else:
        print('You Win!')

    # playagain = input('Do you want to play again?(y/n)')
    # if playagain.lower() == 'y':
    #     return rps()
    # else:
    #     print('Thank you for playing!')
    while True :
        playagain = input('Do you want to play again?(y/n)')
        if playagain not in ('y','n'):
            print('Option doesn\'t exist')
            continue
        else:
            break
    if playagain.lower() == 'y':
        return rps()
    else:
        print('Thank you for playing!')

rps()