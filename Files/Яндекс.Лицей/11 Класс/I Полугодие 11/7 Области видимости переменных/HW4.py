data = list()


def setup_profile(name, vacation_dates):
    global data
    data = list()
    data.append(name)
    data.append(vacation_dates)


def print_application_for_leave():
    print("Заявление на отпуск в период", data[1] + ".", data[0])


def print_holiday_money_claim(amount):
    print("Прошу выплатить", amount, "отпускных денег.", data[0])


def print_attorney_letter(to_whom):
    print("На время отпуска в период", data[1], "моим заместителем назначается", to_whom + ".", data[0])
