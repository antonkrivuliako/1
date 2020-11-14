""" Модуль для отримання даних про рух основних засобів та вивід їх на екран
"""

def get_order():
    """ Повертає вміст файла "order.txt" у вигляді списка
    Returns:
        order - список рядків файла
    """

    with open('./data/order.txt', encoding="utf8") as order_file:
        order_list = order_file.readlines()

    # Накопичувач руху основних засобів
    order_drive = []

    for line in order_list:
        line_list = line.split(';')
        line_list[2] = line_list[2][:-1]  # Видаляє '\n' в кінці
        order_drive.append(line_list)


    return order_drive


def show_order(order):
    """ Виводить список руху основних засобів
    Args:
        move_means (list): список руху основних засобів
    """

    # Задати інтервал виводу
    order_code_from = input("З якого кода виду засобів виводити?")
    order_code_to = input("По який код виду засобів виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for order in order:
        if order_code_from <= order[1] <= order_code_to:
            print("Клієнт: {:13} Номер заказа: {:2} Код: {:10} Кількість: {:10}".format(order[0], order[1], order[2], order[3]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту товару нічого не знайдено.")


order = get_order()
show_order(order)



def get_dovidnik():
    """ Повертає вміст файла "dovidniks.txt" у вигляді списка
    Returns:
        dovidnik_list - список рядків файла
    """

    with open('./data/dovidnik.txt', encoding="utf8") as dovidnik_file:
        dovidnik_list = dovidnik_file.readlines()

    # Накопичувач довідника основних засобів
    dovidnik_drive = []

    for line in dovidnik_list:
        line_list = line.split(';')
        line_list[2] = line_list[2][:-1]
        dovidnik_drive.append(line_list)


    return dovidnik_drive


def show_dovidnik(dovidnik):
    """ Виводить список довідника
    Args:
        dovidniks (list): список довідника
    """

    # Задати інтервал виводу
    dovidnik_code_from = input("З якого кода довідника виводити?")
    dovidnik_code_to = input("По який код довідника виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for dovidnik in dovidnik:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print("Код: {:2} Назва: {:25} Вартість {:20}".format(dovidnik[0], dovidnik[1], dovidnik[2]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту довідникіка нічого не знайдено.")


dovidnik = get_dovidnik()
show_dovidnik(dovidnik)
