str = input()

max = 0
for i in range(len(str)):
    if int(str[i]) > max:
        max = int(str[i])
print(max)
