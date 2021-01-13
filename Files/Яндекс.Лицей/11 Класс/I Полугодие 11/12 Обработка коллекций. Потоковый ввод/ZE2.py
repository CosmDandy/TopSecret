s = {}
for i in range(int(input())):
    b = input().lower()
    a = ''.join(sorted(b))
    s[a] = s.get(a, set())
    s[a].add(b)
c = []
for i in s.values():
    if len(i) > 1:
        c.append(' '.join(sorted(i)))
print('\n'.join(sorted(c)))