def decimal_translator_2(number, base):
    try:
        int(number, base)
    except ValueError:
        return None
    else:
        return int(number, base)
