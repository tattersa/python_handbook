n = int(input())

count = 0
for i in range(n):
    str = input()
    if "Зайка" in str or "зайка" in str:
        count += 1
print(count)
