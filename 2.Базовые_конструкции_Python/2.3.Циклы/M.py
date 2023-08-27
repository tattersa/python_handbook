n = int(input())

name = ""
for i in range(n):
    str = input()
    if len(name) == 0:
        name = str
    elif str < name:
        name = str

print(name)
