# import random module
import random

# digit map

digitMap = {

    'zero':   '0',
    'one' :   '1',
    'two' :   '2',
    'three' : '3',
    'four':   '4',
    'five':   '5',
    'six':    '6',
    'seven':  '7',
    'eight':  '8',
    'nine':   '9'

}

def convert(userInput):

    # empty number var
    number = ''

    # iterates through user input, and uses the input to convert alphabetical representations into numerical
    for char in userInput:

        # adds the character into the previously empty number variable
        number += digitMap[char]
    
    # converts number variable into an integer
    number = int(number)

    return number

# modularity if run in repl
if __name__ == '__main__':

    # random list
    randomList = 0
    convert()