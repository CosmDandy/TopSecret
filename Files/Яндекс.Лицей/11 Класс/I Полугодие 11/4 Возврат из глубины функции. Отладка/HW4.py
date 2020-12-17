shops = {'Шестёрочка': {'Консервы': ['Ананасы кусочками', 'Ананасы колечками'],
                        'Сухофрукты': ['Тропические ананасы', 'Дуриан вяленый'],
                        'Фрукты': ['Бананы', 'Манго']},
         'Микси': {'Овощи-фрукты': ['Яблоки', 'Груши', 'Личи']}}


def search_fruit(shops, fruit):
    for shop, deps in shops.items():
        for dep, items in deps.items():
            if fruit in items:
                return shop, dep
    return None, None


print(*search_fruit(shops, 'Дуриан'))
