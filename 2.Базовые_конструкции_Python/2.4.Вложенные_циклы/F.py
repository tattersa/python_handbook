list = []
for i in range(n := int(input())):
    list.append(num := int(input()))


def get_greatest_common_divisor(n1, n2):
    if n1 < n2:
        n1, n2 = n2, n1
    while (n1 != 0 and n2 != 0):
        r1 = n1 % n2
        n1 = r1
        if (n1 == 0):
            break
        r2 = n2 % r1
        n2 = r2
    return max(n1, n2)


while len(list) >= 2:
    list.append(get_greatest_common_divisor(list.pop(), list.pop()))

print(list[0])
