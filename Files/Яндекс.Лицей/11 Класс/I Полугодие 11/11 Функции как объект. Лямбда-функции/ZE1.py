def ask_password(login, password, success, failure):
    gl = filter(lambda x: x.lower() in 'aeiouy', password)
    gl1 = list(map(lambda x: x.lower(), gl))
    a = filter(lambda x: x.lower() in 'bcdfghjklmnpqrstvwxz', password)
    b = list(map(lambda x: x.lower(), a))
    log = filter(lambda x: x.lower() in 'bcdfghjklmnpqrstvwxz', login)
    log1 = list(map(lambda x: x.lower(), log))
    if len(gl1) == 3 and (b == log1):
        success(login)
        return True, ''
    if len(gl1) == 3 and (b != log1):
        failure(login, 'Wrong consonants')
        return False, 'Wrong consonants'
    if len(gl1) != 3 and (b == log1):
        failure(login, 'Wrong number of vowels')
        return False, 'Wrong number of vowels'
    if len(gl1) != 3 and (b != log1):
        failure(login, 'Everything is wrong')
        return False, 'Everything is wrong'


def failure(login, b):
    return


def success(login):
    return


def main(login, password):
    a, b = ask_password(login, password, success, failure)
    if not a:
        print('Кто-то пытался притвориться пользователем ' + login.lower() + ', но в пароле '
                                                                             'допустил ошибку: ' + b.upper() + '.')
    else:
        print('Привет, ' + login.lower() + '!')
