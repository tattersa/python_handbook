n = int(input())


def check_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True


sum = 0
for i in range(n):
    number = int(input())
    if check_palindrome(number):
        sum += 1

print(sum)
