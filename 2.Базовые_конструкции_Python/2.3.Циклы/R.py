n = int(input())


def get_prime_numbers(n, prime):
    for i in range(2, n):
        while n % i == 0:
            prime.append(i)
            n /= i


prime = []
get_prime_numbers(n, prime)
is_first = True
for x in prime:
    if is_first:
        print(x, end="")
        is_first = False
    else:
        print(" *", x, end="")
