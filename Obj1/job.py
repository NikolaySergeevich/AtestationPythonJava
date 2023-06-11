from contact import *
from funcshion import *

def beginning():
    
    try:
        start()
        print('Теперь можем начать рабоать.')
        print('Ознакомтесь с возможностями программы и введите подходящий номер.')
        help()
    except:
        print('У вас нет ещё заметок. Давайте их создадим!')
        add_note()
        save()
        print('Теперь в вашем списке заметок есть одна заметка.\n\
Ознакомтесь с возможностями программы и введите подходящий номер.')
        help()

def operate():
    while True:
        num = enter_num('\nВы в главном меню. Введите номер задачи: ')
        if num == 1:
            show_all_notes()
        elif num == 2:
            add_note()
            save()
        elif num == 3:
            remove_note()
            print(' ')
        elif num == 4:
            fixing_note()
            print(' ')
        elif num == 5:
            load()
            print(' ')
        elif num == 6:
            save()
            print(' ')
        elif num == 7:
            ending()
            break
        elif num == 8:
            find_note()
        elif num == 9:
            help()
        else:
            print('Такого функцианала нет. Обратитесь к /help.\n\
Для этого введите число 8')

