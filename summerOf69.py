def summerOf69(arr):

    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while add != True:
            if num != 9:
                break
            else:
                add = True
                break
    print(total)


summerOf69([1, 3, 5])
summerOf69([4, 5, 6, 7, 8, 9])
