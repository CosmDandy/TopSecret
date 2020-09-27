answer = "1"
while answer != "OK":
    a = input()
    b = input()
    if len(a) >= 8:
        if ("123") not in a:
            if b == a:
                answer = "OK"
                print(answer)
            else:
                print("Различаются.")
        else:
            print("Простой!")
    else:
        print("Короткий!")
