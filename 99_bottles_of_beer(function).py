# Simple program for printing out 99 Bottles of Beer lyrics, but with function calls!


def sing():
    # Loops through the numbers from 99 to 0 and prints the lyrics
    # with the corresponding number, calling below function for relevant plural
    # or singular version of word 'bottle' when necessary.
    for i in range(99, 0, -1):
        if i > 1:
            print(f'\n{i} {bottle_number(i)} of beer on the wall. {i} {bottle_number(i)} of beer.'      
                  f'\nTake one down, pass it around, {i-1} {bottle_number(i-1)} of beer on the wall.')
        else:
            print(f'\nNo bottles of beer on the wall. No bottles of beer.'               
                  f'\nGo to the store, buy some more, {99} bottles of beer on the wall!')


def bottle_number(bottles):
    # Returns the correct bottle word.
    if bottles in range(2, 100):
        return f'bottles'
    elif bottles == 1:
        return f'bottle'
    else:
        return f'bottles'


sing()
