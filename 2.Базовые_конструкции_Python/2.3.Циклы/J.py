x = 0
y = 0
while (str := input()) != "СТОП":
    steps = int(input())
    if str == "СЕВЕР":
        y += steps
    elif str == "ВОСТОК":
        x += steps
    elif str == "ЮГ":
        y -= steps
    elif str == "ЗАПАД":
        x -= steps
print(y)
print(x)
