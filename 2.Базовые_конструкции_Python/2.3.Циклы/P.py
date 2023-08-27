n = input()


def check_palindrome(n):
    for i in range(len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True


if check_palindrome(n):
    print("YES")
else:
    print("NO")
