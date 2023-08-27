n = int(input())

result = ""

for i in range(n):
    max = 0
    number = input()
    for j in range(len(number)):
        if int(number[j]) > max:
            max = int(number[j])
    result += str(max)

print(result)
