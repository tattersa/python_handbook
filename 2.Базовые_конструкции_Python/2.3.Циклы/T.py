n = int(input())
h_previous = 0

wrong = -1
for i in range(n):
    b = int(input())
    h_current = b % 256
    m = b // 256 ** 2
    r = b // 256 % 256
    # print("m = ", m, "r = ", r, "h_current = ", h_current, "h_prev = ", h_previous)
    if h_current >= 100 or h_current != (37 * (m + r + h_previous)) % 256:
        wrong = i
        break
    else:
        h_previous = h_current

print(wrong)
