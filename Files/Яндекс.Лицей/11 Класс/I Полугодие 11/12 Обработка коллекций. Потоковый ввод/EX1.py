words = input().split()
words = sorted(words, key=lambda x: x.lower())
print(' '.join(words))
