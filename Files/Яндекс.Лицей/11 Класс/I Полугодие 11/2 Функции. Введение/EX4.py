def who_are_you_and_hello():
    flag = True
    name = None
    while flag:
        name = input()
        if name == name.capitalize() and name.isalpha():
            flag = False
            print("Привет, " + name + "!")
