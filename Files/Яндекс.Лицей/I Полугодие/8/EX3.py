x = int(input())
x1 = 0
y = -1
answer = -1
while x1 < x:
    y += 1
    x1 = 2 ** y
    answer += 1
if x1 == x:
    print(answer)
else:
    print("НЕТ")
