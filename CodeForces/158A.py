firstLine = input().split(" ")
n = int(firstLine[0])
k = int(firstLine[1])

secondLine = input().split(" ")
score = secondLine[k-1]

if int(score) > 0:
    remainingScores = secondLine[k:]
    remainingScoreCount = remainingScores.count(score) # suppose the k'th person's score is 5 and 2 people have 5, then this will return 1.

    advance = k + (remainingScoreCount)

    print(advance)
else:
    advance = 0
    for x in secondLine:
        if int(x) > 0:
            advance += 1
            
    print(advance)
