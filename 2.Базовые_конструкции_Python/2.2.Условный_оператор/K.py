n = input()

max_index = 0
if n[1] >= n[2] and n[1] > n[max_index]:
    max_index = 1
elif n[2] > n[1] and n[2] > n[max_index]:
    max_index = 2

min_index = 0
if n[1] <= n[2] and n[1] < n[min_index]:
    min_index = 1
elif n[2] < n[1] and n[2] < n[min_index]:
    min_index = 2

# print(max_index, min_index)
indexes = [0, 1, 2]
indexes.remove(max_index)
indexes.remove(min_index)

medium_index = indexes.pop()

if int(n[min_index]) + int(n[max_index]) == int(n[medium_index]) * 2:
    print("YES")
else:
    print("NO")
