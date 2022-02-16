# main function
def paperDoll(txt):

    result = ''
    # for loop, iterates through the string
    for char in txt:

        # for every character in the string, create it but multiply by 3
        result += char*3

    # print result
    print(result)


paperDoll('Hello!')
paperDoll('Wow')
paperDoll('Python is fun!')
