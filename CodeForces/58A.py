message = input()

h_count = message.count("h")
h_index = 0
find = "helloX"

success = False

for _ in range(h_count):
    current_min_index = message.index("h", h_index)

    currentFoundIndex = 0
    currentCheck = find[currentFoundIndex]

    for letterIndex in range(len(message)):
        if message[letterIndex] == currentCheck and letterIndex >= current_min_index:
            currentFoundIndex += 1
            currentCheck = find[currentFoundIndex]
            current_min_index = letterIndex
    
    if currentFoundIndex == 5:
        success = True
        break


if success == True:
    print("YES")
else:
    print("NO")