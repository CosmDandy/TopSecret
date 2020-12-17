def mirroring():
    global environment
    environment = environment.split(" ")
    a1 = list()
    a2 = list()
    if len(environment) % 2 == 0:
        x = len(environment) // 2
    else:
        x = int(len(environment) / 2)
    for i in range(x):
        a1.append(environment[i])
    for i in range(x, len(environment)):
        a2.append(environment[i])
    a1 = sorted(a1, key=len)
    a2 = sorted(a2, key=len, reverse=True)
    environment = " ".join(a1 + a2)
