def month_name(x, name):
    ru = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь",
          "октябрь", "ноябрь", "декабрь"]
    en = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
          "october", "november", "december"]
    if name == "en":
        return en[x - 1]
    else:
        return ru[x - 1]
