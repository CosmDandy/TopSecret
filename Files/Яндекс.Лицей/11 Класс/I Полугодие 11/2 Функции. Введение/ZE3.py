def bracket_check(test_string):
    x1 = x2 = 0
    x = list(test_string)
    if test_string == "":
        print("YES")
    elif test_string[0] == ")":
        print("NO")
    else:
        for j in range(len(test_string)):
            if "(" in test_string[j]:
                x1 += 1
            else:
                x2 += 1
        if x1 == x2:
            for i in range(len(x)):
                if not x:
                    print("YES")
                    break
                elif x[0] == "(":
                    n = 1
                    while x[n] != ")":
                        n += 1
                        if n > len(x):
                            print("NO")
                            break
                    else:
                        del x[0]
                        del x[n - 1]
                else:
                    print("NO")
                    break
        else:
            print("NO")
