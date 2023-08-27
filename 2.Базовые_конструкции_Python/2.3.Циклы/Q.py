n = input()

result = ""

for i in range(len(n)):
    if int(n[i]) % 2 == 1:
        result += n[i]
    # if int(n[i]) % 2 == 1:
    #     result += n[i]

print(result)
