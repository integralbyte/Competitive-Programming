myinput = input()

if myinput == "{}":
    print(0)
else:
    inputArr = myinput.replace("{", "").replace("}", "").split(", ")

    mydict = []
    unique = 0

    for letter in inputArr:
        if letter not in mydict:
            mydict.append(letter)
            unique += 1

    print(unique)