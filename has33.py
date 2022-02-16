# main function
def has33(nums):

    # iterates through the list and tries to find two 3s next to each other
    for i in range(0, len(nums) - 1):

        # if indice i has a 3 and the indice next to it has a 3, print true
        if nums[i] == 3 and nums[i + 1] == 3:
            return print('True')

    return print('False')


has33([1, 3, 3])
has33([3, 1, 3])
has33([3, 3, 3])
has33([1, 3, 1, 3])
