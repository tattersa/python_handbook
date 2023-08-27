n = int(input())


def check_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[len(x) - i - 1]:
            return False
    return True

    
if check_palindrome(n):
    print("YES")
else:
    print("NO")
