import rps
import guess_number

def game_select(name):
    try:
        user_selection = int(input(f'''{name} choose a game:\n1 = Rock Paper Scissors\n2 = Guess My number\n'''))

        user_validation = (1,2)

        if user_selection not in user_validation:
            print(f'Please enter a valid option, {name}')
            return game_select(name)
        elif user_selection == user_validation[0]:
            play = rps.rps_game(name)
        else:
            play = guess_number.guess(name)

        play()

    except ValueError:
        print(f'Please enter a valid number,{name}')
        game_select(name)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Please Provide your name.'
    )

    parser.add_argument('-n', '--name',metavar='name',required=True,help='Enter your name.')

    args = parser.parse_args()

    play = game_select(args.name)