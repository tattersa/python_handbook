sum = 0
while (cost := float(input())) != 0:
    if cost >= 500:
        sum += cost * 0.9
    else:
        sum += cost
print(f"{sum:.1f}")
