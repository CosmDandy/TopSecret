def check_password(password):
    def decore(fun):
        def new_fun(*args, **kwargs):
            if password == 'пароль':
                return fun(*args, **kwargs)
            print('В доступе отказано')
        return new_fun
    return decore
