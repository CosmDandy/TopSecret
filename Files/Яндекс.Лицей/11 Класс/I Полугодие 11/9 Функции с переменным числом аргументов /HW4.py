def circuit_resistance(*data, connection='serial', conductivity=False):
    if connection == 'serial':
        R = sum(data)
    else:
        R = 0
        for i in data:
            R += 1 / i
        R = 1 / R
    if not conductivity:
        return R
    else:
        return 1 / R