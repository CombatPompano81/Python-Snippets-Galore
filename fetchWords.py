from urllib.request import urlopen


def fetchWords():

    story = urlopen('http://sixty-north.com/c/t.txt')
    storyWords = []

    for line in story:

        lineWords = line.decode('utf-8').split()

        for word in lineWords:
            storyWords.append(word)

    story.close()

    for word in storyWords:
        print(word)

    if __name__ == '__main__':
        fetchWords()
