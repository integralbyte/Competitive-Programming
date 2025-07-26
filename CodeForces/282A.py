totalOperations = int(input())

x = 0

for i in range(totalOperations):
    currentOperation = input()
    if currentOperation == "++X" or currentOperation == "X++":
        x += 1
    elif currentOperation == "--X" or currentOperation == "X--":
        x -= 1

print(x)
