import random

LANGUAGE = 'en'


def return_chars(flag: str) -> str:
    """Ф. переключатель языка"""
    if LANGUAGE == 'ru':
        return 'уеаоэию' if flag == 'b' else 'йцкнгшщзхфвпрлджчсмтб'
    else:
        return 'aeiouy' if flag == 'a' else 'bcdfghjklmnpqrstvwxz'


def get_random_num(x=1, y=2) -> int:
    return random.randint(x, y)


def get_char(flag: int) -> str:
    """Если флаг == 1 ф. генерирует гласный символ, либо 1 или 2 согласных, случайным образом"""
    if flag == 1:
        return random.choice(return_chars('a'))
    else:
        res = ''
        for _ in range(get_random_num()):
            res += random.choice(return_chars('b'))
        return res


def create_name() -> str:
    """Ф. генерит имя в параметре get_random_num указана длина имени.
        num - переключатель гласных/согласных букв"""
    gen_name = []
    num = get_random_num()
    for _ in range(get_random_num(3, 7)):
        gen_name.append(get_char(num))
        num = 2 if num == 1 else 1
    return "".join(gen_name).title()


def create_list_names(quantity: int, language='en') -> list[str]:
    """Передаем в ф. кол-во и язык(можно не указывать, по дефолту='en' и есть 'ru')"""
    global LANGUAGE
    LANGUAGE = language
    return [create_name() for _ in range(quantity)]


if __name__ == '__main__':
    print(create_name())
    res1 = create_list_names(100, 'ru')
    for name in res1:
        print(name)