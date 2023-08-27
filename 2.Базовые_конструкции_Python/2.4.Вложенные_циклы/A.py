n = int(input())

for i in range(1, n + 1):
    is_first = True
    for j in range(1, n + 1):
        if is_first:
            is_first = False
            print(i * j, end="")
        else:
            print(" ", i * j, sep="", end="")
    print()
