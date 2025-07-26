import math

totalForces = int(input())

x_force = 0
y_force = 0
z_force = 0

for _ in range(totalForces):
    vector = list(map(int, input().split(" ")))
    x_force += vector[0]
    y_force += vector[1]
    z_force += vector[2]


if x_force == 0 and y_force == 0 and z_force == 0:
    print("YES")
else:
    print("NO")