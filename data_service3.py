"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""

"""модуль зчитує первинні файли для обробки
"""


def get_dovidniks():
    """повертає список клієнтів b з файла `dovidniks.txt`

    Returns:
        dovidniks_list: список клієнтів
    """

    with open('./data/dovidniks.txt', encoding="utf8") as dovidniks_file:
        from_file = dovidniks_file.readlines()

    dovidniks_list = []
    for line in from_file:
        line_list = line.split(';')
        dovidniks_list.append(line_list)

    return dovidniks_list


def get_orders():
    """повертає список накладних

    Returns:
        from_file: список накладних
    """

    with open('./data/orders.txt', encoding="utf8") as orders_file:
        from_file = orders_file.readlines()

    # розбити строку на реквізити та перетворити формати (при потребі)

    # список-накопичувач
    orders_list = []

    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = int(line_list[4])
        orders_list.append(line_list)

    return orders_list


def show_dovidniks(dovidniks):
    """виводить список клієнтів по заданому інтервалу кодів

    Args:
        dovidniks (list): список клієнтів
    """

    # задати інтервал виводу
    dovidnik_code_from = input("З якого кода довідника? ")
    dovidnik_code_to = input("По який код довідника? ")

    lines_found = 0

    for dovidnik in dovidniks:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print("код: {:5} назва: {:15} адреса: {:25}".format(*dovidnik))
            lines_found += 1

    if lines_found == 0:
        print("Клієнтів по Вашому запиту не знайдено")


def show_orders(orders):
    """виводить список накладних на екран

    Args:
        orders (list): список накладних
    """

    for order in orders:
        print("код клієнта: {:3} номер заказу {:4} код товару: {:20} кількість: {:3}"
              .format(order[0], order[1], order[2], order[3]))

# clients = get_clients()
# show_clients(clients)

# orders = get_orders()
# show_orders(orders)
