def upperLower(str):

    amountOfUpper = 0
    amountOfLower = 0

    for letter in str:
        if letter.isupper():
            letter = 1
            amountOfUpper = letter + amountOfUpper
        elif letter.islower():
            letter = 1
            amountOfLower = letter + amountOfLower

    print(f'Amount of uppercase letters: {amountOfUpper}')
    print(f'Amount of lowercase letters: {amountOfLower}')


upperLower('Hello Mr.Rodgers, how are you doing this fine Tuesday?')
upperLower('Python can sometimes be frustrating, but keep on PUSHING!')
