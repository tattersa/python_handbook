b = int(input())
total = int(input())


def from_bynary_to_decimal(b):
    result = 0
    for x in range(len(str(b))):
        result += b % 10 * (2 ** x)
        b = b // 10
    return result
    

print(total - from_bynary_to_decimal(b))
