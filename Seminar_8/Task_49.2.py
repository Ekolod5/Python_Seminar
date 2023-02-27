# Задача N49. Создать телефонный справочник с возможностью импорта и экспорта 
# данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, 
# которые должны находиться в файле.
# 1. Программа должна выводить данные;
# 2. Программа должна сохранять данные в текстовом файле;
# 3. Пользователь может ввести одну из характеристик для 
# поиска определенной записи (Например имя или фамилию человека);
# 4. Использование функций. Ваша программа не должна быть линейной.

#  Фамилия, имя, отчество, номер телефона


def ask_user():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = int(input('Введите номер телефона: '))  # Можно сделать валидацию, проверку
    return last_name, first_name, phone_number             # кортеж


def save_to_file(data: tuple, file, mode ='a'):            # mode - можно другую переменную название
    data_str = ' '.join(map(str, data))    
    with open(file, mode, encoding='utf-8') as fd:         # 'cp-1251' Windows
        fd.write(f'{data_str}\n')                          # конструкция with open закроет без close

# Запись в файл (параметр mode) методом:'a' - если у нас был файл мы допишем новые данные в конец; если не было, запишем новые данные. 
# 'w' - если у нас был файл мы все сотрем и запишем новые данные; если не было, запишем новые данные.


def read_file(file):
    with open(file, 'r', encoding='utf-8') as fd:  # 'r' - чтение
        lines = fd.readlines()
    headers = ['фамилия', 'имя', 'номер телефона']
    list_contacts = []
    for line in lines:
        line = line.strip().split()
        list_contacts.append(dict(zip(headers, line)))    # см. Task_1.py
    return list_contacts


def search_contact(list_contacts: list, param: str, what: str):
    param_dict = {'1': 'фамилия', '2': 'имя', '3': 'номер телефона'}
    found_contacts = []
    for contact in list_contacts:
        if contact[param_dict[param]] == what:
            found_contacts.append(contact)
    return found_contacts


def ask_search():
    print('По какому полю выполнить поиск?')
    search_param = input('1 - по фамилии, 2 - по имени, 3 - по номеру телефона: ')
    what = None
    if search_param == '1':
        what = input('Введите фамилию для поиска: ')
    elif search_param == '2':
        what = input('Введите имя для поиска: ')
    elif search_param == '3':
        what = input('Введите номер для поиска: ')
    return search_param, what


def main_menu():
    file_contacts = 'file.txt'
    while True:
        user_choice = input('1 - добавить новый контакт,\n '
                            '2 - найти контакт,\n 3 - посмотреть весь справочник,\n 0 - выйти\n')
        if user_choice == '1':
            # print('добавить новый контакт')
            save_to_file(ask_user(), file_contacts)
        elif user_choice == '2':
            # print('найти контакт')
            lst_contacts = read_file(file_contacts)
            search_param, what = ask_search()
            res = search_contact(lst_contacts, search_param, what)
            print(res)
        elif user_choice == '3':
            # print('посмотреть весь справочник')
            print(read_file(file_contacts))
        elif user_choice == '0':
            print('До свидания')
            break


if __name__ == '__main__':

    main_menu()
    # data = ask_user()
    # print(data)
    # save_to_file(data, 'w')
    # save_to_file(data, file_contacts)
    # lst_contacts = read_file(file_contacts)
    # print(lst_contacts)
    # search_param, what = ask_search()
    # res = search_contact(lst_contacts, search_param, what)
    # print(res)

# CSV:
# https://docs.python.org/3/library/csv.html
# https://docs-python.ru/standart-library/modul-csv-python/priemy-raboty-modulem-csv/
# SQLite:
# https://docs-python.ru/standart-library/modul-sqlite3-python/brief-description/
# https://docs.python.org/3/library/sqlite3.html