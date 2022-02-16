# go here we
# fun this will be :)

# master yoda function
def masterYoda(text):

    # split into seperate inidces in a list
    textList = text.split()

    # reverse
    reverseText = textList[::-1]
    final = ' '.join(reverseText)

    # console to print
    print(final)


masterYoda("We are ready")
