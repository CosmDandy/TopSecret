n = int(input())
x = 0
for i in range(n):
    a = input()
    if "Кот" in a:
        x += 1
    elif "кот" in a:
        x += 1
if x >= 1:
    print("МЯУ")
else:
    print("НЕТ")
