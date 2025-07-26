import math

length = int(input())
childrenArr = list(map(int, input().split(" ")))

taxis = 0

fourCount = childrenArr.count(4)
taxis += fourCount
childrenArr = [x for x in childrenArr if x != 4]

oneCount = childrenArr.count(1)
emptySeats = childrenArr.count(3) + 2*childrenArr.count(2)
while True:
    if oneCount >= emptySeats:
        extraSeats = oneCount - emptySeats
        extraTaxis = math.ceil(extraSeats/4)

        taxis += childrenArr.count(3) + childrenArr.count(2) + extraTaxis
        break

    else:
        emptySeatsThrees = childrenArr.count(3)
        remainingOneCounts = 0
        if oneCount >= emptySeatsThrees:
            remainingOneCounts = oneCount - emptySeatsThrees
            taxis += childrenArr.count(3)
        else:
            taxis += childrenArr.count(3)
            taxis += math.ceil(childrenArr.count(2)/2)
            break
        
        emptySeatsTwos = 2*childrenArr.count(2)

        if remainingOneCounts >= emptySeatsTwos:
            remainingOneCounts = oneCount - emptySeatsTwos
            taxis += childrenArr.count(2)
        else:
            twoTaxisFilled = math.ceil(remainingOneCounts/2)
            taxis += twoTaxisFilled

            remainingTwoTaxis = emptySeatsTwos/2 - twoTaxisFilled
            taxis += math.ceil(remainingTwoTaxis/2)
            break


        
print(taxis)
