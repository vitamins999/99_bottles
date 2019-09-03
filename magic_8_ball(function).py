# Simple Magic 8 Ball program.  User asks a question and it gives a random answer.

from random import choice
import time
import sys


def ask_question():
    """User asks question and Magic 8 Ball replies."""
    while True:
        question = input('What would you like to ask me?\n\n')
        if question == '':
            print('You didn\'t ask anything!\n')
            continue
        print('Thinking....')
        time.sleep(3)
        print(choice(eight_ball))
        repeat_play()


def repeat_play():
    """Asks the user if they want to play again."""
    while True:
        play_again = input('\nWould you like to ask another question? (y/n)\n\n').lower()
        if play_again == 'n' or play_again == 'no':
            sys.exit()
        elif play_again == 'y' or play_again == 'yes':
            ask_question()
        else:
            print('\nThat is not a valid answer!')


eight_ball = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.',
]

print(f'Hi, I\'m the Magic 8 Ball!')
ask_question()
