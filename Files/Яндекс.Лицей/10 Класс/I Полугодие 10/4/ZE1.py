print("Как ваши дела ?")
a = input()
if (("хорош" in a) or ("прекрас" in a)) and (("?" not in a) and ("не" not in a)):
    print("Отлично, у меня тоже всё хорошо :)")
elif "плох" in a and (("?" not in a) and ("не" not in a)):
    print("Ничего, скоро всё наладится")
elif ("?" in a) or ("не" in a):
    print("Извини, я не понимаю")
else:
    print("Ошибка")