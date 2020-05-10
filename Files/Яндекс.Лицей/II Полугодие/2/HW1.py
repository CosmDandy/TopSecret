x = input()
key = 1
end = x[-1]
start = end
while key != 0:
    x = input()
    start = x[0]
    if start == end:
        end = x[-1]
        continue
    else:
        key = 0
        print(x)
