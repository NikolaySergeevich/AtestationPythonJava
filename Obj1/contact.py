from datetime import datetime
#метод ввода числа
def enter_num(text):
    try:
        return int(input(text))
    except:
        return print('\nВведены некоретные данные')
    
#метод ввода текстовой информации
def enter_text():
    text = input('Введите текст: ')
    return text

#МЕТОД ввода даты
def enter_data():
    date = []
    print('\nВведите день(от 1 до 31)')
    day = enter_num('Введите число: ')
    try:
        if day >= 1 and day <=31:
            date.append(str(day))
        elif day < 1 or day > 31:
            print('Вы ввели не существующий день. При поиске день не будет учитан.')
            date.append('.')
    except:
        print('При поиске день не будет учитан.')
        date.append('.')

    print('\nВведите месяц(от 1 до 12)')
    month = enter_num('Введите число: ')
    try:
        if month >= 1 and month <=12:
            date.append(str(month))
        elif month < 1 or month > 12:
            print('Вы ввели не существующий месяц. При поиске месяц не будет учитан.')
            date.append('.')
    except:
        print('При поиске месяц не будет учитан.')
        date.append('.')

    print('\nВведите год')
    year = enter_num('Введите число: ')
    courency_year = datetime.now().year
    try:
        if year >= 1 and year <= courency_year:
            date.append(str(year))
        elif year < 1 or year > courency_year:
            print('Вы ввели не существующий год. При поиске год не будет учитан.')
            date.append('.')
    except:
        print('При поиске год не будет учитан.')
        date.append('.')
    return date


