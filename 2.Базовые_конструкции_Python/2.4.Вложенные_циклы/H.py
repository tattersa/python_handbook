n = int(input())

name = ""
result = 0
for i in range(n):
    name_b = input()
    number = input()
    sum = 0
    for j in range(len(number)):
        sum += int(number[j])
    if sum >= result:
        result = sum
        name = name_b
print(name)

