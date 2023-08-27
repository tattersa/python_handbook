max = 1001
min = 1
medium = (max - min) // 2
print(medium)

while (command := input()) != "Угадал!":
    if command == "Меньше":
        max = (max + min) // 2
        print((max + min) // 2)
    elif command == "Больше":
        min = (max + min) // 2
        print((min + max) // 2)
