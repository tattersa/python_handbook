n = int(input())


def check_prime(n):
    if n <= 1:
        return False
    count = 0
    for i in range(2, n):
        while n % i == 0:
            count += 1
            if count >= 2:
                return False
            n / i
    return True


sum = 0
for i in range(n):
    number = int(input())
    if check_prime(number):
        sum += 1

print(sum)
