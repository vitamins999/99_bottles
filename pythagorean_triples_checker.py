# A program that asks the user to input three values for sides of a triangle
# and then tells the user whether it's a Pythagorean triple or not.

import sys


def ask_user():
    """Asks the user for input, handling Value Errors where appropriate.
    If a Value Error is found, the user is asked to enter that value again.
    The correct values are added to a list and sorted by highest number first,
    then passed to the next function."""

    num_list = []
    error_message = '\nThat is not a number. Let\'s try this again.'

    while True:
        try:
            num_1 = float(input('\nWhat is the first number?  '))
        except ValueError:
            print(error_message)
        else:
            while True:
                try:
                    num_2 = float(input('\nWhat is the second number?  '))
                except ValueError:
                    print(error_message)
                else:
                    while True:
                        try:
                            num_3 = float(input('\nWhat is the third number?  '))
                        except ValueError:
                            print(error_message)
                        else:
                            num_list.extend([num_1, num_2, num_3])
                            num_list.sort(reverse=True)
                            calculate_triangle(num_list[0], num_list[1], num_list[2])


def calculate_triangle(side_1, side_2, side_3):
    """Uses Pythagoras's' Theorem to determine whether the values passed
    make a valid Pythagorean Triangle."""

    if side_1**2 == side_2**2 + side_3**2:
        print(f'\nA triangle with the sides {side_1}, {side_2} and {side_3} is a Pythagorean Triple! Huzzah!')
    else:
        print(f'\nA triangle with the sides {side_1}, {side_2} and {side_3} is NOT a Pythagorean Triple.  Sorry.')
    play_again()


def play_again():
    """Asks user if they want to try another triangle."""

    while True:
        answer = input('\nWould you like to try another triangle? (y/n)  ').lower()
        if answer == 'n' or answer == 'no':
            sys.exit()
        elif answer == 'y' or answer == 'yes':
            ask_user()
        else:
            print('That is not a valid answer!')


print('This program will tell you if a triangle is a Pythagorean Triple.')
ask_user()
