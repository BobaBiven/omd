import random
import time
import math


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️ \n'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Утка взяла зонтик \nУзнаем, идет ли дождь \n...')
    time.sleep(1.5)
    if random.randint(0, 2) == 0:
        print('Не идет, ну и ладно, зонт лишним не бывает')
    else:
        print('Идет, зонт пригодился')
    return 0


def step2_no_umbrella():
    print('Утка не взяла зонтик \nУзнаем, идет ли дождь \n ...')
    time.sleep(1.5)
    if random.randint(0, 2) == 0:
        print('Не идет, повезло')
    else:
        print('Идет, стоит ли за ним вернуться?')
        option = ''
        options = {'да': True, 'нет': False}
        while option not in options:
            print('Выберите: {}/{}'.format(*options))
            option = input()

        if options[option]:
            return step3_came_back()
        return step3_not_came_back()


def step3_not_came_back():
    print('Утка замерзла и заболела, очень жаль!')
    return 0


def step3_came_back():
    # случайные коэффициенты в уравнении далее
    a = random.randint(2, 11)
    b = random.randint(1, 11)
    c = random.randint(1, 11)

    # тут проверка на ровно 2 корня (лень прописывать остальные случаи)
    while b**2 - 4 * a * c <= 0:
        a = random.randint(2, 11)
        b = random.randint(1, 11)
        c = random.randint(1, 11)

    print('Утка ззабыла пароль от домофона, помогите ей войти в подъезд')
    print(f'Чтобы ввойти в подъезд нужно ввести решения уравнения: '
          f'{a}x^2 + {b}x + {c} = 0 (2 знака после запятой)')

    x_1, x_2 = get_quadratic_equation_roots(a, b, c)
    a, b = [float(x) for x in input().split()]

    while (round(max(x_1, x_2), 2) != max(a, b)
           or round(min(x_1, x_2), 2) != min(a, b)):
        print('Попробуйте еще раз')
        a, b = [float(x) for x in input().split()]

    print('Спасибо за помощь, у утки все прекрасно!')
    return 0


def get_quadratic_equation_roots(a, b, c):
    return ((-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a),
            (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a))


if __name__ == '__main__':
    step1()
