import gui
import actions


def work():
    p = gui.path_file()
    print('Что желаем сделать:\n\
    1 - Прочитать справочник;\n\
    2 - Записать справочник;\n\
    3 - Поиск в справочнике;\n\
    4 - Удалить запись')
    act = int(input('Выберие действие --> '))
    if act == 1:
        data = actions.export_data(p)
        actions.print_file(data)
        # actions.read_file(p)
    elif act == 2:
        actions.write_in_file(p)
    elif act == 3:
        actions.new_find(p)
        # actions.find_in_file(p)
    elif act == 4:
        actions.delete_in_file(p)
