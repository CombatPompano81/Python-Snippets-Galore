# animal crackers function
def animalCrackers(text):

    # splits the sentence given and makes a list out of it
    wordList = text.upper().split()

    # logic
    if wordList[0][0] == wordList[1][0]:
        print("True")
    else:
        print("False")


animalCrackers('Levelheaded Llama')
animalCrackers('Crazy Kangaroo')
animalCrackers('scruffy silicon')
