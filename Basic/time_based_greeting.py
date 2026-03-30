import os
os.system("cls")


import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)
minutes=time.strftime('%S')
print(minutes)


if 0 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 16:
    print("Good Afternoon")
elif 16 <= hour < 20:
    print("Good Evening")
else:
    print("Good Night")


