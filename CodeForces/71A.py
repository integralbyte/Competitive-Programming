totalLines = int(input())

for i in range(totalLines):
    currentWord = input()
    if len(currentWord) > 10:
        firstLetter = currentWord[0]
        lastLetter = currentWord[len(currentWord) - 1]
        print(firstLetter + str(len(currentWord) - 2) + lastLetter)
    else:
        print(currentWord)


    