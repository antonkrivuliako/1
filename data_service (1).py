""" Модуль для отримання даних про рух основних засобів та вивід їх на екран
"""

def get_dovidnyk():
    """ Повертає вміст файла "dovidnyk.txt" у вигляді списка
    Returns:
        move_mean_list - список рядків файла
    """

    with open('./data/dovidnyk.txt', encoding="utf8") as dovidnyk_file:
        dovidnyk_list = dovidnyk_file.readlines()

    # Накопичувач руху основних засобів
    dovidnyk_drive = []

    for line in dovidnyk_list:
        line_list = line.split(';')
        line_list[2] = line_list[2][:-1]  # Видаляє '\n' в кінці
        dovidnyk_drive.append(line_list)


    return dovidnyk_drive


def show_dovidnyks(dovidnyks):
    """ Виводить список руху основних засобів
    Args:
        dovidnyk (list): список руху основних засобів
    """

    # Задати інтервал виводу
    dovidnyk_code_from = input("З якого кода товару виводити?")
    dovidnyk_code_to = input("По який код товару виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for dovidnyk in dovidnyks:
        if dovidnyk_code_from <= dovidnyk[0] <= dovidnyk_code_to:
            print("Код: {:6} : {:17} Знижка: {:5}".format(dovidnyk[0], dovidnyk[1], dovidnyk[2]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту товару нічого не знайдено.")


dovidnyks = get_dovidnyk()
show_dovidnyks(dovidnyks)

def get_order():
    """ Повертає вміст файла "order.txt" у вигляді списка
    Returns:
        order_list - список рядків файла
    """

    with open('./data/order.txt') as order_file:
        order_list = order_file.readlines()

    # Накопичувач довідника основних засобів
    order_drive = []

    for line in order_list:
        line_list = line.split(';')
        line_list[3] = line_list[3][:-1]
        order_drive.append(line_list)


    return order_drive


def show_orders(orders):
    """ Виводить список довідника
    Args:
        orders (list): список довідника
    """

    # Задати інтервал виводу
    order_code_from = input("З якого кода довідника виводити?")
    order_code_to = input("По який код довідника виводити?")

    # Накопичує кількість виведених рядків
    kol_lines = 0

    for order in order:
        if order_code_from <= order[0] <= order_code_to:
            print("Код: {:6} Вид: {:6} Код: {:6} Вид: {:6}".format(order[0], order[1], order[2], order[3]))
            kol_lines += 1

    # Перевірити чи був вивід хочаб одного рядка
    if kol_lines == 0:
        print("По Вашому запиту товарообігу нічого не знайдено.")


orders = get_order()
show_orders(orders)
