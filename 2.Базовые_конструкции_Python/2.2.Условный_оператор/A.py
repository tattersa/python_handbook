name = input()
status = input()
print("Как Вас зовут?")
print(f"Здравствуйте, {name}!")
print("Как дела?")
if status == "хорошо":
    print("Я за вас рада!")
elif status == 'плохо':
    print("Всё наладится!")
