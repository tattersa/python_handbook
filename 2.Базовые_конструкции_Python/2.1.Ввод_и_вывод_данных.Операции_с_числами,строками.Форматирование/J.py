pupil = input()
code = int(input())

pupil_number = code % 10
bed_number = code // 10 % 10
group_number = code // 100

print(f"Группа №{group_number}.")
print(f"{pupil_number}. {pupil}.")
print(f"Шкафчик: {code}.")
print(f"Кроватка: {bed_number}.")
print()
