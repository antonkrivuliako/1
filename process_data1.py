""" розрахунок заявок на товари по магазину
"""

from data_service3 import get_dovidniks, get_orders

# словник в якому будуть накопичуватись результати розрахунків
zajavka = {
    'namet_name'    : '',     # назва товару  
    'order_number'  : '',   # номер заказа
    'kod_сlient'    : '',      # код кліента 
    'kol'           : 0,     # кількість
    'price'         : 0.0,   # ціна
    'total'         : 0.0    # сума
}

def create_zajavka():
    """формування списку заявок по магазину на основі вхідних файлів
    """
    dovidniks = get_dovidniks()
    orders = get_orders()

    def get_dovidnik_name(dovidnik_code):
        """повертає назву довідника по його коду
        Args:
            dovidnik_code : код довідника
        Returns:
            dovidnik_name: називає довідника
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[1]

        return "*** назва не знайдена"           

    # список заявк по магаину, що формується
    zajavka_list = []

    # обробляємо послідовно кожний рядок 'orders`
    for order in orders:
        
        # підготувати робочий словник для рядка `order`
        zajavka_copy = zajavka.copy()

        # заповнити робочий словник значеннями з `order`
        zajavka_copy['namet_name'] = order[2]
        zajavka_copy['order_number']  = order[1]
        zajavka_copy['kod_сlient']    = order[3]
        zajavka_copy['price']  = order[4]
        zajavka_copy['total']  = zajavka_copy['kol'] * zajavka_copy['price']
        zajavka_copy['dovidnik'] = get_dovidnik_name(order[0])

        zajavka_list.append(zajavka_copy)

    return zajavka_list


# result = create_zajavka()

# for line in  result:
#     print(line)