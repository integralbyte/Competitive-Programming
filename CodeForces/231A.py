totalProblems = int(input())

solvable = 0

for i in range(totalProblems):
    currentProblem = input()
    list = currentProblem.split(" ")
    if list.count("1") >= 2:
        solvable += 1

print(solvable)
