def encrypt_caesar(msg, shift=3):
    res = ''
    for i in msg:
        if i in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            res += chr((((ord(i) - 1040) + shift) % 32) + 1040)
        elif i in 'йцукенгшщзхъфывапролджэячсмитьбю':
            res += chr((((ord(i) - 1072) + shift) % 32) + 1072)
        else:
            res += i
    return res


def decrypt_caesar(msg, shift=3):
    res = ''
    for i in msg:
        if i in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
            res += chr((((ord(i) - 1040) - shift) % 32) + 1040)
        elif i in 'йцукенгшщзхъфывапролджэячсмитьбю':
            res += chr((((ord(i) - 1072) - shift) % 32) + 1072)
        else:
            res += i
    return res
