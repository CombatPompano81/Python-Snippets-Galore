# import random module
import random

# compliment list
compliments = ['Amazing!', 'Great Work!', 'Fantastic!',
               "Incredible!", "Nice Job!", "Excellent!", "Stupendous!"]

# global score var
# this will be useful when we use it in functions.
score = 0

# main function


def quizQuestion(guess, answer):

    # here is where we put the global score in place
    global score

    # we define a still guessing function to see if the player is still trying.
    stillGuessing = True

    # attempt counter, user will have 3 attempts to solve each question.
    attempt = 0

    # check

    # while the user is stillGuessing and the number of attempts completed are less than 3, execute the check logic.
    while stillGuessing and attempt < 3:

        # ignores case to make code smarter and UI much better
        if guess.lower() == answer.lower():

            # if guess is correct, print out a compliment and add 1 to the score var
            print(f"{random.choice(compliments)}")
            score += 1

        elif attempt < 2:

            # show a motivational message to try again, and shows how many attempts are remaining
            guess = (
                f"Try Again! I know you can do it! \n Number of guesses remaining --> {attempt} \n")

            # add one to attempt counter
            attempt == attempt + 1

    # if attempt == 3, show correct answer
    if attempt == 3:
        print(
            f"Oops, looks like all your attempts are gone! The correct answer was {answer}")

# question creation begins here


# first question
question1 = input('What is the biggest country in the world? \n')
quizQuestion(question1, 'Russia')

# second question
question2 = input('Which country makes the most coffee in the world? \n')
quizQuestion(question2, 'Brazil')

# print score, just for fun
outroMessage = f'Your score is... --> {score}'
print(outroMessage)
