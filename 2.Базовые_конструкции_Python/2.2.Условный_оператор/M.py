n1 = int(input())
n2 = int(input())
n3 = int(input())

if n1 % 10 == n2 % 10 and n1 % 10 == n3 % 10:
    print(n1 % 10)
else:
    print(n1 // 10)
