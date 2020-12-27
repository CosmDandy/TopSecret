def translate(text):
    x = list(s for s in text if s not in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ,.:;-')
    x = "".join(x).split(" ")
    for i in range(x.count("")):
        x.remove("")
    global translated_text
    translated_text = " ".join(x)
