# main function
def lesserOfTwoEvens(numA, numB):
    # checks if num a and num b are even or not
    if numA % 2 == 0 and numB % 2 == 0:
        
        return min(numA, numB)
    else:
        # if one or both numbers are odd, this else statement will execute
        return max(numA, numB)

# check
print(lesserOfTwoEvens(2, 4))
print(lesserOfTwoEvens(2, 5))
