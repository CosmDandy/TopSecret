def spam(name, email, data, city='Калуга'):
    print(f'To: {email}')
    print(f'Здравствуйте, {name}!')
    print(f'Были бы рады видеть вас на встрече начинающих программистов в {city},')
    print(f'которая пройдет {data}.')


spam('kondr', '@icloud.com', '66.66.6666')
spam('kondrashin', '@icloud.com', '13.13.1313')
