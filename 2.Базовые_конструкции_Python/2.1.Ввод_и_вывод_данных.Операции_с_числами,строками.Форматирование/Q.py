d = int(input())
b = int(input())

result = 0
for x in range(len(str(b))):
    result += b % 10 * (2 ** x)
    b = b // 10
result += d
print(result)
