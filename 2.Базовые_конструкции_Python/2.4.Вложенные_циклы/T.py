n = int(input())

max_sum = len(str(n))
ss = 10

for i in range(2, 11):
    copy = n
    sum = 0
    while copy != 0:
        sum += copy % i
        copy = copy // i
    if sum > max_sum:
        ss = i
        max_sum = sum
    elif sum == max_sum and i < ss:
        ss = i

print(ss)
