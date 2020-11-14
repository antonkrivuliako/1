""" модуль для отримання даних про постачання та вивід їх на екран
"""

def get_dovidnik():
    """ повертає вміст файла 'dovidnik.txt` у вигляді списка
    """

    with open('./data/dovidnik.txt', encoding="utf8") as dovidnik_file:
        from_file = dovidnik_file.readlines()

    # накопичувач магазинiв
    dovidnik_list = []

    for line in from_file:
        line_list = line.split(';')
        dovidnik_list.append(line_list)
    return dovidnik_list

def get_orders():
    """ повертає вміст файла 'orders.txt` у вигляді списка
    """
    with open('./data/orders.txt', encoding="utf8") as orders_file:
        from_file = orders_file.readlines()

    orders_list = []

    for line in from_file:
        line_list = line.split()
        line_list[2] = line_list[2][:-1]
        orders_list.append(line_list)

def show_dovidnik(dovidnik):
    # задати інтервал виводу
    dovidnik_code_from = input("З якого кода довідника? ")
    dovidnik_code_to   = input("По який код довідника? ")

    # накопичує кількість виведених рядків
    kol_lines = 0

    for dovidnik in dovidnik:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print("код: {:3} назва: {:16} вартість {:20}".format(dovidnik[0], dovidnik[1], dovidnik[2]))
            kol_lines += 1

    # перевірити чи був вивід хоча б одного рядка
    if kol_lines == 0:
        print("По вашому запиту довідників не знайдено")

dovidnik = get_dovidnik()
show_dovidnik(dovidnik)