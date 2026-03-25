from random import randint

def guess(name):

    game_counter = 0
    user_wins = 0

    def guess_game():
        try:
            user_input = int(input(f'{name}, guess which number I\'m thinking of... 1,2, or 3.\n'))
        except ValueError:
            print(f'{name}, Please enter a number.')
            return guess_game()

        choices = (1,2,3)

        if user_input not in choices:
            print('Please enter 1, 2, or 3.')
            return guess_game()

        python_choice = randint(1,3)

        print(f'{name}, you chose {user_input}.' )
        print(f'I was thinking about the number {python_choice}.')
        nonlocal game_counter
        game_counter += 1
        nonlocal user_wins

        if user_input == python_choice :
            print(f'{name}, you win!')
            user_wins += 1
        else:
            print(f'Sorry, {name}. Better luck next time. 😢')

        print(f'Game Count: {game_counter}')
        print(f'{name}\'s Wins: {user_wins}')
        print(f'Your winning percentage: {user_wins/game_counter*100:.2f}')

        while True:
            play_again = input(
         f'''Play again, {name}\nY for Yes or\nQ for Quit\n''')

            if play_again.lower() == 'y':
                return guess_game()
            elif play_again.lower() == 'q':
                print(f'Thank you for playing!')
                print(f'Bye {name}! 👋')
                break
            else:
                print(f'{name} ,Please enter Y for Yes or Q for Quit.')
                continue

    return guess_game

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Please Provide your name.'
    )

    parser.add_argument('-n', '--name',metavar='name',required=True,help='Enter your name.')

    args = parser.parse_args()

    play = guess(args.name)
    play()