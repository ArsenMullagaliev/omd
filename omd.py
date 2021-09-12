from random import randint

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()

def get_weather():
    weather = {0: 'солнечно', 1: 'дождь', 2: 'ураган'}
    key = randint(0,2)
    return weather[key]

def step2_umbrella():
    umbrella_taken = True
    print('Может, прогноз погоды посмотрим?')
    option = ''
    option2 = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        forecast = get_weather()
        print(f'Обещают {forecast}. Всё равно зонт брать?')
        while option2 not in options:
            print('Выберите: {}/{}'.format(*options))
            option2 = input()
        if not options[option2]:
            umbrella_taken = False
    else:
        forecast = False
        umbrella_taken = True

    weather = get_weather()
    outcome(forecast, weather, umbrella_taken)

def step2_no_umbrella():
    umbrella_taken = False
    print('Может, прогноз погоды посмотрим?')
    option = ''
    option2 = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        forecast = get_weather()
        print(f'Обещают {forecast}. Может всё-таки зонт взять?')
        while option2 not in options:
            print('Выберите: {}/{}'.format(*options))
            option2 = input()
        if options[option2]:
            umbrella_taken = True
    else:
        forecast = False

    weather = get_weather()
    outcome(forecast, weather, umbrella_taken)


def outcome(forecast, weather, umbrella_taken):
    if umbrella_taken:
        if weather == 'солнечно': message = 'Ну хоть голову не напечёт!'
        if weather == 'дождь': message = 'Вот и зонт пригодился!'
        if weather == 'ураган': message = 'Унесло утку на зимовку вместе с зонтом.'
        if forecast:
            if weather != forecast: message += ' А вместо прогноза лучше в следующий раз в окно посмотреть!'
            if weather == forecast:
                weather = f'и правда {weather}'
                message += ' Прогноз-то сбылся!'
        print(f'Утка взяла зонт и пошла, а на улице {weather}. {message}')

    else:
        if weather == 'солнечно': message = 'Хорошо, и крылья не заняты!'
        if weather == 'дождь': message = 'Вот бы сейчас зонт пригодился!'
        if weather == 'ураган': message = 'Зонт бы тут и не помог.'
        if forecast:
            if weather != forecast: message += ' А вместо прогноза лучше в следующий раз в окно посмотреть!'
            if weather == forecast:
                weather = f'и правда {weather}'
                message += ' Прогноз-то сбылся!'
        print(f'Утка не стала зонт брать, а на улице {weather}. {message}')

if __name__ == '__main__':
    step1()