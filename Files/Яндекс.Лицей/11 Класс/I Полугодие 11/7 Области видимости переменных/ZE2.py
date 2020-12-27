import sys
import time


def update_progress(progress):
    barLength = 30  # Modify this to change the length of the progress bar
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
    block = int(round(barLength * progress))
    text = "\rPercent: [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block),
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


def main():
    print(
        "\n1 - Кодирование в код Морзе\n2 - Декодирование кода Морзе\n3 - Скачать базу с Pastebin\n0 ""- Выйти")
    x = int(input())
    while x != "1" or x != "2" or x != "3" or x != "0":
        x = int(input())


print()
print("Запустить программу ?\n1 - Да\n0 - Нет")
x = input()
if x == "Да" or x == "да" or x == "1":
    start()
    main()
elif x == "Нет" or x == "нет" or x == "0":
    print("Отключение от окружения...")
    time.sleep(1)
else:
    print("...")
