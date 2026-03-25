import random
from enum import Enum

def rps_game(name):

    game_counter = 0
    user_wins = 0
    python_wins = 0

    def rps():

        class stats(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3

        print(f'Welcome {name} to the Game Hope you have fun playing!')

        user_inputs = int(input(
            '''
            Enter your choice:
            1.Rock
            2.Paper
            3.Scissors
            '''))

        python_inputs = int(random.choice('123'))

        if user_inputs not in (1, 2, 3):
            print('The provided option is not valid')
            return rps()  # recursion so it will start the game
        if user_inputs in (1, 2, 3):
            print(f'{name} choose' + ' ' + str(stats(user_inputs)).replace('stats.', ''))
            print('Python choose' + ' ' + str(stats(python_inputs)).replace('stats.', ''))


        def decide_winner(user_input,python_input):

            nonlocal user_wins
            nonlocal python_wins

            if user_input == python_input:
                return 'Tie!'
            elif user_input == 1 and python_input == 2:
                python_wins += 1
                return 'You loose!'
            elif user_input == 2 and python_input == 3:
                python_wins += 1
                return 'You loose!'
            elif user_input == 3 and python_input == 1:
                python_wins += 1
                return 'You loose!'
            else:
                user_wins += 1
                return 'You Win!'

        print(decide_winner(user_inputs,python_inputs))

        nonlocal game_counter
        game_counter += 1

        print('Time\'s played:'+' '+str(game_counter))
        print(f'{name} Wins:{user_wins}')
        print('Python Wins:'+ " "+str(python_wins))

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
            print(f'Thank you for playing!{name}')
            return None
    return rps # This will create a closure

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='''
        Please enter your Name'''
    )

    parser.add_argument('-n','--name',required=True,metavar='name',help='Enter your Name')

    args = parser.parse_args()

    play = rps_game(args.name) # using a closure rps_game provide the values it required and rps will take it
    play() # This we need to call