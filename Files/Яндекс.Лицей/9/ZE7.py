print("Привет пользователь !")
answer = "?"
while answer != "Пока":

    if "муз" in answer or "компьют" in answer \
            or "ест" in answer or "друг" in answer:

        if "муз" in answer:
            print("Какой ваш любимый жанр в музыке ?")
            print("Вот я например предпочитаю Synthwave и Retrowave")
            answer = input()
            if "Synthwave" in answer or "Retrowave" in answer:
                print("У нас схожие вкусы и я считаю что это просто прекрасно")
            elif answer == "Пока":
                print("Досвидания")
                break
            else:
                print("Я тоже ингода слушаю песни этого жанра")
            print("Вы играете на каких нибудь инструментах ?")
            answer = input()
            if "Да" in answer or "да" in answer:
                print("Это очень здорово, вы молодец !")
                print("Хотите поговорить о чем-то еще ?")
                answer = "?"
            elif "Нет" in answer or "не" in answer:
                print("A хотели бы научиться ?")
                answer = input()
                if "Да" in answer or "да" in answer:
                    print("А на каком инструменте ?")
                    answer = input()
                    print("Интересно")
                    print("Хотите поговорить о чем-то еще ?")
                    answer = "?"
                elif "Нет" in answer or "не" in answer:
                    print("А почему ?")
                    answer = input()
                    print("Ясно")
                    print("Хотите поговорить о чем-то еще ?")
                    answer = "?"
                elif answer == "Пока":
                    print("Досвидания")
                    break
                else:
                    print("Понятно")
                    print("Хотите поговорить о чем-то еще ?")
                    answer = "?"
            elif answer == "Пока":
                print("Досвидания")
                break
            else:
                print("Понятно")
                print("Хотите поговорить о чем-то еще ?")
                answer = "?"

        elif "компьют" in answer:
            print("Вы знаете что такое микрокомпьютер")
            answer = input()
            if "Да" in answer or "да" in answer:
                print("Ну и что же это такое ?")
                answer = input()
                print("Я бы дал такое определение")
                print(
                    "«Мѝкрокомпью́тер» — термин, обозначавший компьютер, "
                    "выполненный на основе микропроцессора")
                print("Ну а если просто, то это очень маленький компьютер")
                print("А вы знаете об Raspberry Pi ?")
                answer = input()
                if "Да" in answer or "да" in answer:
                    print("Да вы походу гений IT технологий")
                    print("А у вас он есть ?")
                    answer = input()
                    if "Да" in answer or "да" in answer:
                        print("Вы гений IT технологий")
                        print("Хотите поговорить о чем-то еще ?")
                        answer = "?"
                    elif "Нет" in answer or "не" in answer:
                        print("Обязательно купите в ближайщее время !!!")
                        print("Хотите поговорить о чем-то еще ?")
                        answer = "?"
                elif "Нет" in answer or "не" in answer:
                    print(
                        "Это нормально, скоро вы откроете для себя и эту тайну")
                    print("Хотите поговорить о чем-то еще ?")
                    answer = "?"
                elif answer == "Пока":
                    print("Досвидания")
                    break
                else:
                    print("Понятно")
                    print("Хотите поговорить о чем-то еще ?")
                    answer = "?"
            elif "Нет" in answer or "нет" in answer:
                print("Сейчас раскажу")
                print(
                    "«Мѝкрокомпью́тер» — термин, обозначавший компьютер, "
                    "выполненный на основе микропроцессора")
                print("Ну а если просто, то это очень маленький компьютер")
                print("Хотите поговорить о чем-то еще ?")
                answer = "?"
                continue
            elif answer == "Пока":
                print("Досвидания")
                break
            else:
                print("Понятно")
                print("Хотите поговорить о чем-то еще ?")
                answer = "?"

        elif "ест" in answer:
            print(
                "Здравствуй Абитуриент! Не получается написать задачу по "
                "информатике,",
                "сидишь уже вторую ночь, а результата нет.",
                "Пересдаешь ее 9-ый раз, но ответ все равно не правильный, "
                "не расстраивайся!!!",
                "Добьет тебя наш тест на знание истории Физтеха.")
            print("Начнем с легких вопросов.")
            print()
            print("Вопрос №1")
            print()
            print(
                "Лев Давидович Ландау, проффесор кафедры теоритической физики.")
            print("В каком году он стал проффесором МФТИ ?")
            print("1. 1956")
            print("2. 1958")
            print("3. 1962")
            print("4. 1964")
            print("5. 1975")
            one = input()
            if one != "1" and one != "2" and one != "3" and one != "4" \
                    and one != "5" and one != "Пока":
                print("Ошибка")
            elif one == "Пока":
                print("Досвидания")
                break
            else:
                if one == "3":
                    one = 1
                else:
                    one = 0
                print()
                print("Вопрос №2")
                print()
                print("Учебный процесс. Как устроен Учебный процесс в МФТИ ?")
                print("В МФТИ действует трехуровневая система подготовки...")
                print("1. Бакалавриат - 3 года и магистратура - 2 года")
                print(
                    "2. Бакалавриат - 3 года и магистратура - 2 года, "
                    "аспирантура 3 или 4 года")
                print(
                    "3. Бакалавриат - 5 года и магистратура - 2 года, "
                    "аспирантура 4 года")
                print(
                    "4. Бакалавриат - 5 года и магистратура - 3 года, "
                    "аспирантура 2 года")
                print("5. Бакалавриат - 4 года и магистратура - 4 года")
                two = input()
                if two != "1" and two != "2" and two != "3" and \
                        two != "4" and two != "5" and two != "Пока":
                    print("Ошибка")
                elif two == "Пока":
                    print("Досвидания")
                    break
                else:
                    if two == "2":
                        two = 1
                    else:
                        two = 0
                    print()
                    print("Вопрос №3")
                    print()
                    print(
                        "Физтех - это превосходство. Это всегда первый класс, "
                        "даже высший класс. Это элита.")
                    print("Кто это сказал ?")
                    print("1. Владимир Фортов")
                    print("2. Андрей Гейм")
                    print("3. Николай Кудрявцев")
                    print("4. Борис Кустодиев")
                    print("5. Алексей Абрикосов")
                    three = input()
                    if three != "1" and three != "2" and three != "3" \
                            and three != "4" and three != "5" \
                            and three != "Пока":
                        print("Ошибка")
                    elif three == "Пока":
                        print("Досвидания")
                        break
                    else:
                        if three == "1":
                            three = 1
                        else:
                            three = 0
                        print()
                        print("Вопрос №4")
                        print()
                        print("Сколько в Физтехе факультетов ?")
                        print("1. 5")
                        print("2. 7")
                        print("3. 9")
                        print("4. 11")
                        print("5. 15")
                        four = input()
                        if four != "1" and four != "2" and four != "3" \
                                and four != "4" and four != "5" \
                                and four != "Пока":
                            print("Ошибка")
                        elif four == "Пока":
                            print("Досвидания")
                            break
                        else:
                            if four == "4":
                                four = 1
                            else:
                                four = 0
                            print()
                            print("Вопрос №5")
                            print()
                            print(
                                "Последний вопрос. Какой средний бал у "
                                "поступающих ?")
                            print("1. 56")
                            print("2. 68")
                            print("3. 72")
                            print("4. 97")
                            print("5. 100")
                            five = input()
                            if five != "1" and five != "2" and five != "3" \
                                    and five != "4" and five != "5" \
                                    and five != "Пока":
                                print("Ошибка")
                            elif five == "Пока":
                                print("Досвидания")
                                break
                            else:
                                if five == "4":
                                    five = 1
                                else:
                                    five = 0

                                answer = int(one) + int(two) + int(three) + int(
                                    four) + int(five)
                                if answer == 5:
                                    print(
                                        "Вы человек вообще ??? Все ответы "
                                        "правильные. Поздравляем !!!")
                                    print("Конец теста")
                                    answer = "?"

                                elif answer == 4:
                                    print(
                                        "Вы немного напутали но все равно "
                                        "большая часть ваших ответов верная. "
                                        " Поздравляем")
                                    print("Конец теста")
                                    answer = "?"

                                elif answer == 3:
                                    print(
                                        "У вас не очень много ошибок, но вы "
                                        "могли и лучше ")
                                    print("Конец теста")
                                    answer = "?"

                                elif answer == 2:
                                    print("Алееееее, ну чо ты, плечи расправь.")
                                    print("Конец теста")
                                    answer = "?"

                                elif answer <= 1:
                                    print("...Нет слов...")
                                    print("Конец теста")
                                    answer = "?"

        elif "друг" in answer:
            print("О чем бы вы хотели поговорить")
            while answer != "Пока" or answer != "?":
                answer = input()
                if "?" in answer:
                    print("Не знаю что ответить")
                    continue
                elif "дел" in answer:
                    print("У меня все просто прекрасно")
                    print("А у вас ?")
                    answer = input()
                    continue
                elif "погод" in answer:
                    print("Я надеюсь что сегодня будет хорошая погода")
                    continue
                elif "О" in answer:
                    print("Отлично")
                    continue
                else:
                    print("Понятно")
                    print("Хотите поговорить о чем-то еще ?")
                    answer = "?"
                    break

    elif answer == "?":
        print()
        print(
            "На какие темы ты бы хотел поговорить ? Выбери пожалуйста из ряда "
            "придложенных.")
        print("О музыке")
        print("О микрокомпьютерах")
        print("Тест на знание МФТИ")
        print("На другую тему")
        print()
        print("? - Темы для разговоров")
        print('"Пока" - чтобы отключить бота')
        print("Введите ответ.")
        answer = input()
    elif "Нет" not in answer or "нет" not in answer or "Да" not in answer \
            or "да" not in answer or "муз" not in answer\
            or "компьют" not in answer \
            or "ест" not in answer or "друг" not in answer:
        answer = input()
        continue
else:
    print("Досвидания")
