n = int(input())
x = 0
for i in range(n):
    a = input()
    if "Кот" in a or "кот" in a:
        print("МЯУ")
        break
else:
    print("НЕТ")
