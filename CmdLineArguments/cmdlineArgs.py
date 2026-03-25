#Cmd line args are used to pass the values from terminal itself by using -n -l whterver we mention in add_arguments
#first thing is to import argsparse
#argparse.ArgumentParser() for description adding
# parser.add_argument to add the arguments like -n -l
# parser.parse_args() to parse the args
def user(name,lang):

    greetings = {
        'English' : 'english',
        'Telugu' : 'telugu',
        'Hindi' : 'hindi'
    }
    msg = f'{name} speaks {greetings[lang]}'
    print(msg)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personal greeting.'
    )

    parser.add_argument(
        '-n', '--name', metavar='name', required=True,
        help='Name of the person to greet.'
    )

    parser.add_argument(
        '-l', '--lang', metavar='language', required=True,
        choices=['English','Telugu','Hindi'],
    )

    args = parser.parse_args()

    user(args.name,args.lang)

    #py cmdlineArgs.py -n 'Ruku' -l 'English' you can't use run cause it requires us to pass in terminal

