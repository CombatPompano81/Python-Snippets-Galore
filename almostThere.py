# main function
def almostThere(num):

    # logic

    # if the absolute value of 100 - n or 200 - n <= 10, then return true
    if (abs(100-num) <= 10) or (abs(200-num) <= 10):
        print('True')
    else:
        # else, print false
        print('False')


almostThere(104)
almostThere(150)
almostThere(209)
