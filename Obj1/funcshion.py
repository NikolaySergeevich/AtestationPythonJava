import json
from contact import *
from datetime import datetime
global notes
notes = {}

def start():
    print('Здравстыуйте, вы открыли приложение для ваших заметок. Меня зовут Note_Bot и я помогу вам найти,\n\
внести новую заметку, удалить необходимую или изменить уже существующую')
    print()
    load()
    
def load():
    global notes
    global max_kyeeee
    with open("D:/Учёба в GB/Промежуточная контрольная работа по блоку специализация/Obj1/notes.json","r",encoding="utf-8") as fh:
        notes=json.load(fh)
        list_whis_kye = []
        for item in notes:
            list_whis_kye.append(item)
        max_kyeeee = max(list_whis_kye)
        print(max_kyeeee)
    print("Ваши заметки были успешно загружены!")

def save():
    with open("D:/Учёба в GB/Промежуточная контрольная работа по блоку специализация/Obj1/notes.json","w",encoding="utf-8") as fh:
        fh.write(json.dumps(notes,ensure_ascii=False))
    print("Ваши заметки были успешно сохранёны в файле notes.json")

def ending():
    save()
    print('\nВы закончили работу с заметками.')

def help():
    tex = '\n\
1 - Просмотреть все заметки\n\
2 - Добавить заметку\n\
3 - Удалить заметку\n\
4 - Редактирование заметки\n\
5 - Загрузить заметки с хронилища\n\
6 - Сохранить заметки в хронилище\n\
7 - Закончить работу с заметками\n\
8 - Найти заметку\n\
9 - Help\n\
    '
    print(tex)

#метод создание ключа
def creat_key():
    global kye_first
    try:   
        with open("D:/Учёба в GB/Промежуточная контрольная работа по блоку специализация/Obj1/notes.json","r",encoding="utf-8") as fh:
            notes=json.load(fh)
            list_whis_kye = []
            for item in notes:
                list_whis_kye.append(int(item))
            max_kyeeee = max(list_whis_kye) 
            max_kyeeee = max_kyeeee + 1
        return max_kyeeee
    except:
        try:
            if kye_first == 1:
                kye_first += 1
                return kye_first
        except:
            kye_first = 1
            return kye_first
       
#метод получения даты с временем
def giv_time():
    time = datetime.now()
    timefin = '{}.{}.{}. {}:{}'.format(time.day, time.month, time.year, time.hour, time.minute)
    return timefin
    

#метод добавления заметки
def add_note():
    try:
        kye = creat_key()
        kyestr = str(kye)
        print('Придумайте заголовок для вашей заметки')
        title = enter_text()
        print('На очереди написать заметку') 
        body = enter_text()
        time =  giv_time()
        note  = {"Заголовок: ":title, "Заметка: ":body, "время добавления/изменения: ":time}
        # print(notes)
        notes[kyestr] = note
    except:
        print('Что-то пошло не так. Поробуйте ещё раз. Для этого введите "2". Или "8", что бы вызвать help')

#метод вывода всего списка заметок
def show_all_notes():
    for(k,v) in notes.items():
        print('№ ', end='')
        print(k)
        for (p,g) in v.items():
            print(p, end='')
            print(g)
        print()
#метод показа одной заметки. Принимает ключ
def show_one_note(num):
    for i in notes:
        if i == num:
            print('\n№ ', end='')
            print(i)
            for (p,g) in notes[i].items():
                print(p, end='')
                print(g,)
            


#метод поиска по названию заметки
def find_note_of_title():
    fint_lst = []
    num = enter_text().lower()
    title = "Заголовок: "
    count = 0
    for i in notes:
        for j in notes[i]:
            if title == j:
                fint_lst.append(i)
                if num == notes[i][j]:
                    count =+1
                    print('№ ', i, '\n', end='')
                    for (p,g) in notes[i].items():
                        print(p, end='')
                        print(g)
                    print()
    if count == 0:
        print('Заметки с таким заголовком нет.')
    return fint_lst

#метод поиска по дате
def find_note_of_date():
    date = enter_data() #список с датой, которую вводит пользователь
    lst_whis_notes = [] #сбда будут складываться ключи заметок подходящиих
    if date[2] != '.':
        lst_whis_notes = help_for_find_note_of_date(2, date)
    else:
        if date[1] != '.':
            lst_whis_notes = help_for_find_note_of_date(1, date)
        else:
            if date[0] != '.':
                lst_whis_notes = help_for_find_note_of_date(0, date)
            else:
                print('Ваш запрос не содержит ни одного значения.')
    if len(lst_whis_notes) == 0:
        print('Поиск не дал результата.')
    else:
        lst_fin = creat_fin_lsr_whis_kye(lst_whis_notes, date)
        if len(lst_fin) != 0:
            for it in lst_fin:
                show_one_note(it)
        else:
            print('Поиск не дал результата.')


#Вспомогательный метод для поиска по дате
def help_for_find_note_of_date(num, date):
    lst_whis_notes = []
    title_date = 'время добавления/изменения: '
    for i in notes:
            for j in notes[i]:
                if j == title_date:
                    lst_whis_date_from_notes = notes[i][j].split('.')
                    if lst_whis_date_from_notes[num] == date[num]:
                        lst_whis_notes.append(i)
    return lst_whis_notes

#вспомогаьельный метод для поиска по дате.
def creat_fin_lsr_whis_kye(lst, date):
    lst_fin = []
    title_date = 'время добавления/изменения: '
    if date[2] != '.' and date[1] != '.' and date[0] != '.':
        for i in lst:
            for j in notes[i]:
                if j == title_date:
                    lst_whis_date_from_notes = notes[i][j].split('.')
                    if lst_whis_date_from_notes[2] == date[2] and lst_whis_date_from_notes[1] == date[1] and lst_whis_date_from_notes[0] == date[0]:
                        lst_fin.append(i)
        return lst_fin
    #ниже 3 случая когда год точно указан
    if date[2] != '.' and date[1] != '.' and date[0] == '.':
        for i in lst:
            for j in notes[i]:
                if j == title_date:
                    lst_whis_date_from_notes = notes[i][j].split('.')
                    if lst_whis_date_from_notes[2] == date[2] and lst_whis_date_from_notes[1] == date[1]:
                        lst_fin.append(i)
        return lst_fin
    if date[2] != '.' and date[1] == '.' and date[0] != '.':
        for i in lst:
            for j in notes[i]:
                if j == title_date:
                    lst_whis_date_from_notes = notes[i][j].split('.')
                    if lst_whis_date_from_notes[2] == date[2] and lst_whis_date_from_notes[0] == date[0]:
                        lst_fin.append(i)
        return lst_fin
    if date[2] != '.' and date[1] == '.' and date[0] == '.':
        for i in lst:
            for j in notes[i]:
                if j == title_date:
                    lst_whis_date_from_notes = notes[i][j].split('.')
                    if lst_whis_date_from_notes[2] == date[2]:
                        lst_fin.append(i)
        return lst_fin
    #ниже 2 случая когда месяц указан точно          
    if date[2] == '.' and date[1] != '.' and date[0] != '.':
        for i in lst:
            for j in notes[i]:
                if j == title_date:
                    lst_whis_date_from_notes = notes[i][j].split('.')
                    if lst_whis_date_from_notes[1] == date[1] and lst_whis_date_from_notes[0] == date[0]:
                        lst_fin.append(i)
        return lst_fin
    if date[2] == '.' and date[1] != '.' and date[0] == '.':
        for i in lst:
            for j in notes[i]:
                if j == title_date:
                    lst_whis_date_from_notes = notes[i][j].split('.')
                    if lst_whis_date_from_notes[1] == date[1]:
                        lst_fin.append(i)
        return lst_fin
    #ниже указаны методы, когда дни указаын точно
    if date[2] == '.' and date[1] == '.' and date[0] != '.':
        for i in lst:
            for j in notes[i]:
                if j == title_date:
                    lst_whis_date_from_notes = notes[i][j].split('.')
                    if lst_whis_date_from_notes[0] == date[0]:
                        lst_fin.append(i)
        return lst_fin
                        

def find_note():
    print('Поиск можно осуществить по заголовку заметки, а так же по дате создания/редактирования.\n\
          Что бы найти заметку по заголовку - введите 1\n\
          Что бы найти заметку по дате - введите 2')
    num = enter_num('Введите номер задачи: ')
    if num == 1:
        find_note_of_title()
    elif num == 2:
        find_note_of_date()
    else:
        print('По другим критериям поиск не просзоводим.')

#метод удаления заметки
def remove_note():
    print('\nУкажите номер заметки, которую хотите удалить.\n')
    show_all_notes()
    indicate = False
    try:
        num =  enter_num('Введите номер заметки: ')
        num = str(num)
        for i in notes:
            if num == i:
                del notes[i]
                indicate = True
                break
        if indicate: print('Заметка успешно удалена.') 
        else: print('Заметки с таким номером не найдено.')
    except:
        print('Пробуйте ещё.')

#метод исправления замтеки
def fixing_note():
    print('\nУкажите номер заметки, которую хотите исправить.')
    show_all_notes()
    indicate = False
    old_title = 'Заголовок: '
    old_text = 'Заметка: '
    try:
        num =  enter_num('Введите номер заметки: ')
        num = str(num)
        for i in notes:
            if num == i:
                show_one_note(i)
                print('\nВведите 1 что бы изменить заголовок заметки.\nВведите 2 что бы изменить саму заметку.')
                num1 = enter_num('\nВведите число: ')
                if num1 == 1:
                    help_for_fixing(old_title, i)
                    indicate = True
                elif num1 == 2:
                    help_for_fixing(old_text, i)
                    indicate = True
                break
        if indicate: print('Заметка успешно изменена.') 
        else: print('Заметки с таким номером не найдено.')
    except:
        print('Пробуйте ещё.')

#вспомогатлеьный метод для внесения изменений
def help_for_fixing(text, key):
    new_title = enter_text()
    for j in notes[key]:
        if j == text:
            notes[key][j] = new_title
        elif j == 'время добавления/изменения: ':
            new_date = giv_time()
            notes[key][j] = new_date