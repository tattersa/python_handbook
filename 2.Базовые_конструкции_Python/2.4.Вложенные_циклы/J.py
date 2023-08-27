print("А Б В")
for i in range(1, (n := int(input())) - 1):
    for j in range(1, n - 1):
        if (n - i - j > 0):
            print(i, j, n - i - j)
