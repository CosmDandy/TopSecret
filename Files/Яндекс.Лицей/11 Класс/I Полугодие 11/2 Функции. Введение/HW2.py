def ask_password():
    flag = 0
    for i in range(3):
        x = input()
        if x == "password":
            flag = 1
            break
    if flag == 1:
        print("Пароль принят")
    else:
        print("В доступе отказано")
