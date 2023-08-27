h = int(input())
m = int(input())
t = int(input())

minutes = t % 60
hours = t // 60

m += minutes
if m >= 60:
    m -= 60
    h += 1

h += hours
if h >= 24:
    h = h % 24

if h < 10:
    h = "0" + str(h)

if m < 10:
    m = "0" + str(m)

  
print(f"{h}:{m}")
