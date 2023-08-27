n1 = int(input())
n2 = int(input())

is_first = True
for i in range(n1, n2 + 1):
    if is_first:
        print(i, sep="", end="")
        is_first = False
    else:
        print(" ", i, sep="", end="")
