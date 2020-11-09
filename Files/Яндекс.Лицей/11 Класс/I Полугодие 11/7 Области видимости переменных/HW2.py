def translate(text):
    x = list()
    for i in range(len(text)):
        for j in range(len(text[i])):
            if text[i][j] not in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ,:;'
            a = (" ".join(text[i]) if text[i][j] not in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ,:;').split(" ")
            x.append(text[i])
