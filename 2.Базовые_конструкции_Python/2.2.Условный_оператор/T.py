n1 = input()
n2 = input()
n3 = input()

strings = [n1, n2, n3]

result = ""
for str in strings:
    if "Зайка" in str or "зайка" in str:
        if len(result) == 0:
            result = str
        elif str < result:
            result = str


print(result, len(result))
