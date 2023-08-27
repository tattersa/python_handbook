n = int(input())

sum = 0
for i in range(n):
    b = input()
    for j in range(len(b)):
        sum += int(b[j])

print(sum)
