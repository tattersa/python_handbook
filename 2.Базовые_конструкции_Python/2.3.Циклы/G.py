n1 = int(input())
n2 = int(input())

prime1 = []
prime2 = []


def get_prime_numbers(n, prime):
    for i in range(2, n + 1):
        while n % i == 0:
            prime.append(i)
            n /= i
            

get_prime_numbers(n1, prime1)
get_prime_numbers(n2, prime2)

result_multipliers = prime1

for x in prime1:
    if x in prime2:
        prime2.remove(x)

for x in prime2:
    result_multipliers.append(x)

result = 1

for x in result_multipliers:
    result *= x

print(result)
