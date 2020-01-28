x = None
sh = 0
sl = 0
sls = None
shs = None
while x != "стоп":
    x = input()
    if x != "стоп":
        if len(x) > sh:
            sh = len(x)
            shs = x
        if len(x) < sh:
            sl = len(x)
            sls = x
    else:
        break
print(sh, sl, shs, sls)
