a = input()
b = input()
bull = 0
cow = 0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            if i == j:
                bull += 1
            else:
                cow += 1
print(bull, cow)