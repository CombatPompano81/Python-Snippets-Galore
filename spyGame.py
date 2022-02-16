def spyGame(arr):

    answer = [0, 0, 7, 'x']
    for num in arr:

        if num == answer[0]:
            answer.pop(0)

    print(len(answer) == 1)


spyGame([1, 2, 4, 0, 0, 7, 5])
spyGame([1, 0, 2, 4, 0, 5, 7])
spyGame([1, 7, 2, 0, 4, 5, 0])
