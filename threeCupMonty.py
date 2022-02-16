# import shuffle namespace / function from built in python random module
from random import shuffle

# shuffle function


def shuffleList(exampleList):
    # importing single commands can be very useful at times, such as right here.
    shuffle(exampleList)
    return exampleList

# due to the nature of this game, if the player guesses randomly, then the odds of choosing the cup with a ball underneath would be 1/3

# player guessing function


def userGuess():

    # default value for guess
    guess = ' '

    # extra variable for the prompt
    prompt = 'Pick a number --> 0, 1, or 2?'

    # extra code to keep asking if the prompt is not answered
    while guess not in ['0', '1', '2']:

        # prompt
        guess = guess = input(prompt)

    # return the value given back from the prompt
    return int(guess)

# automated answer check function, combines both user input and the shuffleList functions we created.


def checkGuess(mylist, guess):

    # check if the guess is correct, or incorrect using if statements
    if mylist[guess] == 'O':
        print("You are correct! Great work!")
    else:
        # in the event that the answer given was incorrect, print out where the ball actually was.
        print("Oops, that was incorrect!")
        print("This is where the ball was...")
        print(mylist)


# create the inital list
mylist = [' ', 'O', ' ']

# shuffles initial ist
myListShuffled = shuffleList(mylist)

# initiates userGuess function and stores it in a variable
guess = userGuess()

# finally, we have to check the guess to see if it is right or not.
checkGuess(myListShuffled, guess)
