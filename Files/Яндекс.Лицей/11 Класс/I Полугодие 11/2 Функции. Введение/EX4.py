def who_are_you_and_hello():
    name = input()
    while name != name.title():
        for i in range(len(name)):
            if "1234567890" in name:
                continue
        name = input()


who_are_you_and_hello()
