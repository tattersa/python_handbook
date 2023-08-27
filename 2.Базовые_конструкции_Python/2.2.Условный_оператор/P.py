petya_speed, vasya_speed, tolya_speed = int(input()), int(input()), int(input())
winner_speed = max(petya_speed, vasya_speed, tolya_speed)
loser_speed = min(petya_speed, vasya_speed, tolya_speed)
if winner_speed == petya_speed:
    winner = 'Петя'
    if loser_speed == tolya_speed:
        loser, second = 'Толя', 'Вася'
    else:
        loser, second = 'Вася', 'Толя'
elif winner_speed == tolya_speed:
    winner = 'Толя'
    if loser_speed == petya_speed:
        loser, second = 'Петя', 'Вася'
    else:
        loser, second = 'Вася', 'Петя'
else:
    winner = 'Вася'
    if loser_speed == tolya_speed:
        loser, second = 'Толя', 'Петя'
    else:
        loser, second = 'Петя', 'Толя'
print(f'{"": ^8}{winner: ^8}{"": ^8}')
print(f'{second: ^8}{"": ^8}{"": ^8}')
print(f'{"": ^8}{"": ^8}{loser: ^8}')
print(f'{"II": ^8}{"I": ^8}{"III": ^8}')
