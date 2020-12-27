def password_level(password):
    if 6 <= len(password):
        if not password.isdigit() and (password.isalpha() and password != password.lower()):
            if password != password.lower() or (password == password.lower() and not password.isalpha()):
                if password.isalnum() and password != password.lower():
                    return "Надежный пароль"
            else:
                return "Слабый пароль"
        else:
            return "Ненадежный пароль"
    else:
        return "Недопустимый пароль"


print(password_level("qwe"))
print(password_level("qwerty"))
print(password_level("123Qwerty"))
print(password_level("Qwerty"))
