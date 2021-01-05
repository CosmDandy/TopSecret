def partial_sums(*s):
    s = list(s)
    for i in range(len(s) - 1, -1, -1):
        s[i] = sum(s[:i + 1])
    s = [0] + s
    return s
