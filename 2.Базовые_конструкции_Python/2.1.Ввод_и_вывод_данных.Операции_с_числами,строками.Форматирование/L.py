n = int(input())
m = int(input())

max_length = max(len(str(n)), len(str(m)))

result = 0
for i in range(max_length):
    result += ((n % 10 + m % 10) % 10) * (10 ** i)
    n = n // 10
    m = m // 10

print(result)
