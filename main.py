GLOBAL_PARSEC_IN_KILOMETERS: float = 30856775814900
GLOBAL_SPEED_OF_LIGHT: float = 299792.458


class Parsec:
    def __init__(self, time_unit: float, name: str):
        self.time_unit = time_unit
        self.name = name

    def show(self: float):
        list_time_unit = [seconds, minutes, hours, days, weeks, months, years, decades, centuries, millennia]
        if self > 0:
            print(f"Что бы преодолеть {PARSEC_INPUT} парсеков, двигаясь со\nскоростью света понадобится:")
            for i in list_time_unit:
                print(f"{round(i.time_unit, 3)} {i.name}")
        elif self == 0:
            print("\033[31m{}".format(f'Парсеки не могут быть равны нулю!'))
            return
        elif self < 0:
            print("\033[31m{}".format(f'Парсеки не могут быть отрицательными!'))
            return
        print(f'\n{PARSEC_INPUT} парсеков = {round(PARSEC_INPUT * GLOBAL_PARSEC_IN_KILOMETERS)} км')
        print('🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣🤣')


try:
    str_show = input("Введите расстояние в парсеках: ")
    PARSEC_INPUT = float(str_show.replace(',', '.'))
    parsecs_input_in_seconds = round((PARSEC_INPUT * GLOBAL_PARSEC_IN_KILOMETERS) / GLOBAL_SPEED_OF_LIGHT)
    seconds = Parsec(parsecs_input_in_seconds, 'секунд')
    minutes = Parsec(parsecs_input_in_seconds / 60, 'минут')
    hours = Parsec(parsecs_input_in_seconds / 3600, 'часов')
    days = Parsec(parsecs_input_in_seconds / 86400, 'дней')
    weeks = Parsec(parsecs_input_in_seconds / 604800, 'недель')
    months = Parsec(parsecs_input_in_seconds / 2.628e+6, 'месяцев')
    years = Parsec(parsecs_input_in_seconds / 3.154e+7, 'лет')
    decades = Parsec(parsecs_input_in_seconds / 3.154e+8, 'десятилетий')
    centuries = Parsec(parsecs_input_in_seconds / 3.154e+9, 'веков')
    millennia = Parsec(parsecs_input_in_seconds / 3.154e+10, 'тысячелетий')
    print('-------------------------------')
    Parsec.show(seconds.time_unit)

except ValueError:
    print("\033[31m{}".format(f'Введены некорректные данные расстояния в парсеках!'))
