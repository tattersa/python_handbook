a = float(input())
b = float(input())
c = float(input())

if a == 0 and b == 0 and c == 0:
    print("Infinite solutions")
elif a == 0 and b == 0 and c != 0:
    print("No solution")
elif a == 0 and b != 0:
    print(f"{-c / b:.2f}")
else:
    d = b * b - 4 * a * c
    if d < 0:
        print("No solution")
    elif d == 0:
        print(f"{-b / 2 / a:.2f}")
    else:
        x1 = (-b + d ** 0.5) / 2 / a
        x2 = (-b - d ** 0.5) / 2 / a
        if (x1 < x2):
            print(f"{x1:.2f} {x2:.2f}")
        else:
            print(f"{x2:.2f} {x1:.2f}")
