counter = 0
while (str := input()) != "Приехали!":
    if "Зайка" in str or "зайка" in str:
        counter += 1
print(counter)
