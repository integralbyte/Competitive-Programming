import math

arr = list(map(int, input().split(" ")))

totalRides = arr[0]
comboRides = arr[1]
singlePrice = arr[2]
comboPrice = arr[3]

comboTickets = (totalRides // comboRides)*comboPrice
singleTickets = (totalRides % comboRides)*singlePrice

price1 = comboTickets+singleTickets
price2 = math.ceil(totalRides / comboRides)*comboPrice
price3 = totalRides*singlePrice

print(min(price1, price2, price3))

