n1 = int(input())
n2 = int(input())
direction = 1
if n2 < n1:
    direction = -1
is_first = True
for i in range(n1, n2 + direction, direction):
    if is_first:
        print(i, sep="", end="")
        is_first = False
    else:
        print(" ", i, sep="", end="")
