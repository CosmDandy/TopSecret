name = None


def polite_input(question):
    global name
    if name is None:
        print("Как вас зовут?")
        name = str(input())
    print(str(name) + ",", question)
    answer = input()
    return answer
