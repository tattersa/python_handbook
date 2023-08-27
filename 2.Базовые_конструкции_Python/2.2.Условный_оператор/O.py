n1 = input()
n2 = input()

n1 += n2

max_index = 0
min_index = 0
for i in range(len(n1)):
    if n1[i] > n1[max_index]:
        max_index = i
    if n1[i] <= n1[min_index]:
        min_index = i
# print(max_index, min_index)
indexes = list(range(0, len(n1)))
indexes.remove(max_index)
indexes.remove(min_index)
medium = str((int(n1[indexes.pop()]) + int(n1[indexes.pop()])) % 10)
print(n1[max_index] + medium + n1[min_index])
