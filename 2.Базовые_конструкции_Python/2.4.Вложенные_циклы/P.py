n = int(input())
m = int(input())


width = len(str(n * m)) + 1
for i in range(1, n + 1):
    is_first = True
    for j in range(1, m + 1):
        if is_first:
            is_first = False
            print(str(i * j).rjust(width), " " * (width - 1), sep="", end="")
        else:
            print("|" + str(i * j).rjust(width), " " * (width - 1), sep="", end="")
    print()
    if i != n:
        print("-" * (m * 2 * width - 1))
print()
