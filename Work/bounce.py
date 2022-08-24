# bounce.py
#
# Exercise 1.5
bounce_height = 100
times = 10
i = 1

while i <= times:
    bounce_height = round(bounce_height * 0.6, 4)
    print(i, end=' ')
    print(bounce_height)
    i = i + 1

