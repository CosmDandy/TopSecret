oldstr = "Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой тренировки - и вы сможете это делать."
newstr = oldstr.replace("ауоыиэяюёеАУОЫИЭЯЮЁЕ,:;", "")
print(newstr)
