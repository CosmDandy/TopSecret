a = input()
words = []
while a != "стоп":
    words.append(a)
    a = input()
ma, mi = max(words, key=len), min(words, key=len)
if set(ma).issuperset(set(mi)):
    print("ДА")
else:
    print("НЕТ")
