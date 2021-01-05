def arithmetic_operation(s):
    if s == '+':
        return lambda a, b: a + b
    elif s == '-':
        return lambda a, b: a - b
    elif s == '*':
        return lambda a, b: a * b
    elif s == '/':
        return lambda a, b: a / b
