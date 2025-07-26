a = int(input())
b = int(input())
c = int(input())

largest = []

largest.append(a+(b*c))
largest.append((a*b)+c)

largest.append(a+(b+c))
largest.append((a+b)+c)

largest.append(a*(b*c))
largest.append((a*b)*c)

largest.append(a*(b+c))
largest.append((a+b)*c)

largest.sort()

print(largest[-1])