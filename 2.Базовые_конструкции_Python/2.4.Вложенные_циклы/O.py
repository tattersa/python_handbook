n = int(input())
m = int(input())

k = 1
width = len(str(n * m))
for i in range(n):
    is_first = True
    for j in range(m):
        if j % 2 == 0:
            result = k + n * j
        else:
            result = (j + 1) * n - i
        if is_first:
            is_first = False
            print(str(result).rjust(width), sep="", end="")
        else:
            print(" ", str(result).rjust(width), sep="", end="")

    print()
    k += 1
