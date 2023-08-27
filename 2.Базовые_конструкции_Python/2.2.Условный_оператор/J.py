n = int(input())

sum1 = n % 10 + n // 10 % 10
sum2 = n // 100 + n // 10 % 10

if sum1 > sum2:
    print(str(sum1) + str(sum2))
else:
    print(str(sum2) + str(sum1))
