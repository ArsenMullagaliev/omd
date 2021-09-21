from random import randint


WEATHER = {0: 'солнечно', 1: 'дождь', 2: 'ураган'}
OPTIONS = {'да': True, 'нет': False}
MESSAGES_UMBRELLA = {
    'солнечно': 'Ну хоть голову не напечёт!',
    'дождь': 'Вот и зонт пригодился!',
    'ураган': 'Унесло утку на зимовку вместе с зонтом.'
}
MESSAGES_NO_UMBRELLA = {
    'солнечно': 'Хорошо, и крылья не заняты!',
    'дождь': 'Вот бы сейчас зонт пригодился!',
    'ураган': 'Зонт бы тут и не помог.'
}


def get_weather():
    key = randint(0,2)
    return WEATHER[key]


def get_option():
    option = ''
    while option not in OPTIONS:
        print('Выберите: {}/{}'.format(*OPTIONS))
        option = input()
    return option


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = get_option()
    umbrella_taken = OPTIONS[option]
    return step2(umbrella_taken)


def step2(umbrella_taken):
    print('Может, прогноз погоды посмотрим?')
    option = get_option()
    if OPTIONS[option]:
        return step3(umbrella_taken)
    else:
        forecast = None
        return outcome(umbrella_taken, forecast)


def step3(umbrella_taken):
    forecast = get_weather()
    if umbrella_taken:
        print(f'Обещают {forecast}. Всё равно зонт брать?')
    else:
        print(f'Обещают {forecast}. Может, взять зонт?')
    option = get_option()
    umbrella_taken = OPTIONS[option]
    return outcome(umbrella_taken, forecast)


def outcome(umbrella_taken , forecast):
    weather = get_weather()

    if umbrella_taken:
        outcome_message = 'Вышла утка с зонтом'
        message = MESSAGES_UMBRELLA[weather]
    else:
        outcome_message = 'Пошла утка без зонта'
        message = MESSAGES_NO_UMBRELLA[weather]

    if (forecast is not None) and (weather != forecast):
        message += ' Вместо прогноза лучше в окно посмотреть!'
    if (forecast is not None) and (weather == forecast):
        weather = f'и правда {weather}'
        message += ' Прогноз-то сбылся!'

    print(f'{outcome_message}, а на улице {weather}. {message}')


if __name__ == '__main__':
    step1()