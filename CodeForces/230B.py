totalCount = int(input())

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


for num in map(int, input().split(" ")):
    sqrtNum = num**0.5
    if int(sqrtNum) == sqrtNum and is_prime(int(sqrtNum)): # if number has an integer square root, e.g. 4,9,16,25
        print("YES")
    else:
        print("NO")
    