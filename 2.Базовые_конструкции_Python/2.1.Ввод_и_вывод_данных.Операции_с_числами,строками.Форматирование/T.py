n = int(input())
m = int(input())
k1 = int(input())
k2 = int(input())

res1 = (m * n - k1 * n) / (k2 - k1)
res2 = n - res1
print(int(res2), int(res1))
