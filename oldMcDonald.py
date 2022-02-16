# old McD's function to spell his name right automated
def oldMacdonald(mcDonald):

    # first half
    firstHalf = mcDonald[:3].capitalize()

    # second half
    secondHalf = mcDonald[3:].capitalize()

    # concatenate and print out to console
    fullName = firstHalf + secondHalf
    print(fullName)


oldMacdonald('macdonald')
