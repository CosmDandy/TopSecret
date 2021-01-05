def password_level(password):
    x1 = x2 = x3 = False
    if len(password) < 6:
        s = "Недопустимый пароль"
        return s
    elif password.isdigit():
        s = "Ненадежный пароль"
        return s
    for i in password:
        if i.isupper():
            x1 = True
        elif i.islower():
            x2 = True
        elif i in "0123456789":
            x3 = True
    if x1 * x2 * x3:
        s = "Надежный пароль"
    elif x1 ^ x2 and not x3:
        s = "Ненадежный пароль"
    else:
        s = "Слабый пароль"
    return s
