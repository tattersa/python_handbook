n = int(input())
m = int(input())

k = 1
width = len(str(n * m))
is_even = True
for i in range(n):
    is_first = True
    for j in range(m):
        if i % 2 == 0:
            result = k
        else:
            result = (i + 1) * m - j
        if is_first:
            is_first = False
            print(str(result).rjust(width), sep="", end="")
        else:
            print(" ", str(result).rjust(width), sep="", end="")
        k += 1
    print()
