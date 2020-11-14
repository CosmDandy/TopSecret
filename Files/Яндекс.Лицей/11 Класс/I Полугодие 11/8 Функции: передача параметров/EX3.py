def count_vowels(word):
    return len([word[i] for i in range(1, len(word), 2) if word[i] in 'aouiey'])


def secret_sort(secret_avatars):
    secret_avatars[:] = sorted(secret_avatars, key=count_vowels)
