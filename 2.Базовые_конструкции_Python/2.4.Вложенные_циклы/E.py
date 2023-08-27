n = int(input())

sum = 0
for i in range(n):
    count = 0
    while (name := input()) != "ВСЁ":
        if count == 0 and (name == "Зайка" or name == "зайка"):
            count += 1
    sum += count

print(sum)
