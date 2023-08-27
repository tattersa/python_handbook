n = int(input())
m = int(input())

k = 1
width = len(str(n * m))
for i in range(n):
    is_first = True
    for j in range(m):
        if is_first:
            is_first = False
            print(str(k).rjust(width), sep="", end="")
        else:
            print(" ", str(k).rjust(width), sep="", end="")
        k += 1
    print()
