import math

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    alpha = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
elif b > a and b > c:
    alpha = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
else:
    alpha = math.acos((b ** 2 + a ** 2 - c ** 2) / (2 * b * a))

if abs(math.pi / 2 - alpha) < 1e-5:
    print("100%")
elif math.pi / 2 > alpha:
    print("крайне мала")
else:
    print("велика")
