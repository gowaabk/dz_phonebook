import gui


def read_file(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        print(file.read())


def write_in_file(path: str):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(f'{gui.add_contact()}\n')


""" def find_in_file(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        f = file.read().split(';')
        f_name = gui.find_contact()
        for i in f:
            if f_name in i:
                print(i) """


def delete_in_file(path: str):
    with open(path, 'r+', encoding='utf-8') as file:
        f = file.read().split(';')
        f_name = gui.find_contact()
        for i in f:
            if f_name in i:
                f.remove(i)
                print(f'{f} + {f_name}')
                break
    with open(path, 'w', encoding='utf-8') as file:
        file.write(';'.join(f))


def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None


def new_find(path: str):
    word = input('Введите данные для поиска: ')
    data = export_data(path)
    item = search_data(word, data)
    if item != None:
        print('Фамилия'.center(20), 'Имя'.center(20),
              'Телефон'.center(15), 'Примечание'.center(30))
        print('-'*85)
        print(item[0].center(20), item[1].center(20),
              item[2].center(15), item[3].center(30))
    else:
        print('Данные не обнаружены')


def export_data(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        data = []
        t = []
        for line in file:
            if ';' in line:
                temp = line.strip().split(',')
                data.append(temp)
            else:
                data.append(t)
                t = []

    return data


def print_file(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20),
              "Телефон".center(15), "Примечание".center(30))
        print("-"*85)
        for item in data:
            print(item[0].center(20), item[1].center(20),
                  item[2].center(15), item[3].center(30))
    else:
        print("Справочник пуст!")
