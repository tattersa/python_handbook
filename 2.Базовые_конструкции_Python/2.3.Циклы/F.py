n1 = int(input())
n2 = int(input())

max = 1
for i in range(2, min(n1, n2)):
    if n1 % i == 0 and n2 % i == 0:
        max = i
print(max)
