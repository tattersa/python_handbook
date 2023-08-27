n = int(input())

for i in range(n):
    for j in range(3 + i):
        print(f"До старта {3 + i - j} секунд(ы)")
    print(f"Старт {i + 1}!!!")
