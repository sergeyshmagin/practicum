# Импортируйте необходимые модули.
from datetime import datetime

# Укажите два параметра функции:


def validate_record(name, birthdate):
    try:
        datetime.strptime(birthdate, '%d.%m.%Y')
    except ValueError:
        print(
            f'Некорректный формат даты в записи: {name}, {birthdate}'
        )
        return False
    else:
        return True


# Напишите код, верните булево значение.

# Укажите параметры функции:


def process_people(data):
    # Объявите счётчики.
    good_count = 0
    bad_count = 0
    for name, bdate in data:
        if validate_record(name, bdate) is True:
            good_count += 1
        else:
            bad_count += 1
    print(
        f'Некорректных записей: {bad_count}'
    )
    print(
        f'Корректных записей: {good_count}'
    )

    # в каждой паре значений из списка data
    # проверьте корректность формата даты рождения
    # и в зависимости от результата проверки увеличьте один из счётчиков.
    dic = {'good': good_count, 'bad': bad_count}
    return dic


data = [
    ('Иван Иванов', '01.13.2004'),
    ('Пётр Петров', '15.03.1956'),
    ('Зинаида Зеленая', '6 февраля 1997'),
    ('Елена Ленина', 'Второе мая тысяча девятьсот восемьдесят пятого'),
    ('Кирилл Кириллов', '26/11/2003')
]

statistics = process_people(data)
# Выведите на экран информацию о корректных и некорректных записях
# в таком формате:
# Корректных записей: <число>
# Некорректных записей: <число>
