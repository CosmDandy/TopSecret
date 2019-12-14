s = int(input())
x = 0
for i in range(s):
    a = input()
    if "Кот" in a or "кот" in a:
        x += 1
    elif "Пёс" in a or "пёс" in a:
        x = 0
    else:
        continue
if x >= 1:
    print("МЯУ")
else:
    print("НЕТ")
