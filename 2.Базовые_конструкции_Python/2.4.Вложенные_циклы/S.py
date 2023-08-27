n = int(input())

width = len(str((n + 1) // 2)) + 1
for i in range(n):
    for j in range(n):
        if j != n - 1:
            print((f"{min(i, j, n - i - 1, n - j - 1) + 1} ").rjust(width), end="")
        else:
            print((f"{min(i, j, n - i - 1, n - j - 1) + 1}").rjust(width - 1), end="")
    print()


