n = int(input())

max = 1
counter = 0
is_first = True
for i in range(1, n + 1):
    counter += 1
    if is_first:
        print(i, end="")
        is_first = False
    else:
        print(" ", i, sep="", end="")
    if counter >= max:
        counter = 0
        max += 1
        print()
        is_first = True
