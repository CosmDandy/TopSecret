# Никогда не запускать с числами больше 0

a = int(input())
while a > 0:
    print((a ** (a ** a)) ** a)
