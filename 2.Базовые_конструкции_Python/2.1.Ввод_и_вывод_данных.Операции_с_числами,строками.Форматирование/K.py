n = int(input())

first = n % 10
second = n // 10 % 10
third = n // 100 % 10
fourth = n // 1000 % 10

result = third * 1000 + fourth * 100 + first * 10 + second 

print(result)
