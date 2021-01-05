import sys
import time

MorseCode = {}
MorseCode_ru = {"А": "·−", "Б": "−···", "В": "·−−", "Г": "−−·", "Д": "−··", "Е": "·", "Ж": "···−",
                "З": "−−··", "И": "··", "Й": "·−−−", "К": "−·−", "Л": "·−··", "М": "−−", "Н": "−·",
                "О": "−−−", "П": "·−−·", "Р": "·−·", "С": "···", "Т": "−", "У": "··−", "Ф": "··−·",
                "Х": "····", "Ц": "−·−·", "Ч": "−−−·", "Ш": "−−−−", "Щ": "−−·−", "Ъ": "−−·−−",
                "Ы": "−·−−", "Ь": "−··−", "Э": "··−··", "Ю": "··−−", "Я": "·−·−",

                "1": "·−−−−", "2": "··−−−", "3": "···−−", "4": "····−", "5": "·····", "6": "−····",
                "7": "−−···", "8": "−−−··", "9": "−−−−·", "0": "−−−−−", ".": "······", ",": "·−·−·−",
                ":": "−−−···", ";": "−·−·−·", "(": "−·−−·−", ")": "−·−−·−", "'": "·−−−−·",
                '"': "·−··−·", "-": "−····−", "/": "−··−·", "_": "··−−·−", "?": "··−−··",
                "!": "−−··−−", " + ": "·−·−·"}

MorseCode_en = {"A": "·−", "B": "−···", "W": "·−−", "G": "−−·", "D": "−··", "E": "·", "V": "···−",
                "Z": "−−··", "I": "··", "J": "·−−−", "K": "−·−", "L": "·−··", "M": "−−", "N": "−·",
                "O": "−−−", "P": "·−−·", "R": "·−·", "S": "···", "T": "−", "U": "··−", "F": "··−·",
                "H": "····", "C": "−·−·", "Q": "−−·−", "Y": "−·−−", "X": "−··−",

                "1": "·−−−−", "2": "··−−−", "3": "···−−", "4": "····−", "5": "·····", "6": "−····",
                "7": "−−···", "8": "−−−··", "9": "−−−−·", "0": "−−−−−", ".": "······", ",": "·−·−·−",
                ":": "−−−···", ";": "−·−·−·", "(": "−·−−·−", ")": "−·−−·−", "'": "·−−−−·",
                '"': "·−··−·", "-": "−····−", "/": "−··−·", "_": "··−−·−", "?": "··−−··",
                "!": "−−··−−", " + ": "·−·−·"}


def update_progress(progress):
    bar = 25
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(bar * progress))
    text = "\rPercent: [{0}] {1}% {2}".format("#" * block + "-" * (bar - block),
                                              progress * 100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


def start():
    print("Проверка обновлений")
    time.sleep(0.8)
    for i in range(101):
        time.sleep(0.03)
        update_progress(i / 100.0)
    time.sleep(0.6)
    print("Доступ получен.")
    time.sleep(0.8)
    print()
    print("Система взломана. Нанесён урон. Запущено планирование контрмер.")
    time.sleep(0.5)
    print()
    for i in range(101):
        time.sleep(0.012)
        update_progress(i / 100.0)
    for i in range(101):
        time.sleep(0.004)
        update_progress(i / 100.0)
    print()
    for i in range(101):
        time.sleep(0.002)
        update_progress(i / 100.0)
    time.sleep(0.5)
    print()
    print("Военный спутник запущен, коды доступа внутри...")
    time.sleep(2)
    print("Woop-woop! That's the sound of da police!")
    time.sleep(1)
    logo = """
    
    
 /$$      /$$                                                /$$$$$$                  /$$          
| $$$    /$$$                                               /$$__  $$                | $$          
| $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$       | $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$ 
| $$ $$/$$ $$ /$$__  $$ /$$__  $$ /$$_____/ /$$__  $$      | $$       /$$__  $$ /$$__  $$ /$$__  $$
| $$  $$$| $$| $$  \ $$| $$  \__/|  $$$$$$ | $$$$$$$$      | $$      | $$  \ $$| $$  | $$| $$$$$$$$
| $$\  $ | $$| $$  | $$| $$       \____  $$| $$_____/      | $$    $$| $$  | $$| $$  | $$| $$_____/
| $$ \/  | $$|  $$$$$$/| $$       /$$$$$$$/|  $$$$$$$      |  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$
|__/     |__/ \______/ |__/      |_______/  \_______/       \______/  \______/  \_______/ \_______/
    """
    print(logo)
    logo2 = """
               _               ___                       ___                _       
              | |__  _   _    / __\___  ___ _ __ ___    /   \__ _ _ __   __| |_   _ 
              | '_ \| | | |  / /  / _ \/ __| '_ ` _ \  / /\ / _` | '_ \ / _` | | | |
              | |_) | |_| | / /__| (_) \__ \ | | | | |/ /_// (_| | | | | (_| | |_| |
              |_.__/ \__, | \____/\___/|___/_| |_| |_/___,' \__,_|_| |_|\__,_|\__, |
                     |___/                                                    |___/ 
    """
    print(logo2)


def encode_to_morse(text):
    word = []
    sentence = []
    if text != "":
        x = text.upper().split(" ")
        for i in x:
            for j in i:
                y = MorseCode.get(j)
                word.append(y)
            sentence.append(" ".join(word))
            word.clear()
        print("[" + str(text) + "]")
        print("  ".join(sentence))
        print()
        print("Нажмите ENTER чтобы выйти")
    else:
        print("Отключение от сервера...")


def decode_from_morse(code):
    word = []
    sentence = []
    if code != "":
        x = code.split("  ")
        for i in x:
            y = i.split(" ")
            for j in y:
                for k, v in MorseCode.items():
                    if v == j:
                        word.append(k)
            sentence.append("".join(word))
            word.clear()
        print("[" + str(code) + "]")
        print(" ".join(sentence))
        print()
        print("Нажмите ENTER чтобы выйти")
    else:
        print("Отключение от сервера...")


def main():
    x, text, code = None, None, None
    global MorseCode
    while x != 1 or x != 2:
        print("Выбирите язык")
        print("1 - Русский"
              "\n2 - Английский")
        a = int(input())
        if a == 1:
            MorseCode = MorseCode_ru
            break
        elif a == 2:
            MorseCode = MorseCode_en
            break

    while x != 1 or x != 2 or x != 0:
        print("\n1 - Кодирование в код Морзе"
              "\n2 - Декодирование кода Морзе"
              "\n0 - Выйти")
        x = int(input())
        if x == 1:
            print("Кодирование в код Морзе")
            print()
            while text != "":
                text = input()
                encode_to_morse(text)
                print("---------------------")
                print()
            text = None
        elif x == 2:
            print("Декодирование кода Морзе")
            print()
            while code != "":
                code = input()
                decode_from_morse(code)
                print("---------------------")
                print()
            code = None
        elif x == 0:
            print()
            print("Отключение от сервера...")
            time.sleep(1)
            break
        else:
            print("Повторите ввод...")
            continue


print()
print("Запустить программу ?\n1 - Да\n0 - Нет")
s = input()
if s == "Да" or s == "да" or s == "1":
    start()
    main()
elif s == "Нет" or s == "нет" or s == "0":
    print("Отключение от окружения...")
    time.sleep(1)
else:
    print("...")
