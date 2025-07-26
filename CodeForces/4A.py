x = int(input())
y = 0

x_org = x

def checkevens(a, b):
    return a % 2 == 0 and a != 0 and b % 2 == 0 and b != 0

while y != x_org:
    x -=1
    y +=1

    if checkevens(x, y):
        print("YES")
        break

if y == x_org:
    print("NO")