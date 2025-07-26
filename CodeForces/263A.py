currentRow = 0

for i in range(5):
    currentRow += 1
    row = input().split(" ")
    if "1" in row:
        columnNum = row.index("1") + 1
        rowNum = currentRow
        # break. cannot break as remaining rows will not be input and cause an error.

rowOperations = abs(3 - rowNum)
columnOperations = abs(3 - columnNum)

print(rowOperations + columnOperations)