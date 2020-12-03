<<<<<<< HEAD
"""формування заявок на устаткування по магазину
"""

# підключити функції з модуля `data_service111`
from data_service111 import get_dovidnyk, get_order

# структура накопичувача записів вихідних даних
zajavka = {

    'namet_name'   : '',    # назва товару  
    'order_number'   : '',    # номер заказа
    'kod_сlient'  : '',    # код кліента 
    'kol'           : 0,     # кількість
    'price'         : 0.0,   # ціна
    'total'         : 0.0    # сума
}


dovidnyk = get_dovidnyks()
order = get_orders()

def create_zajavka():
    """формування заявок на устаткування
    """
    def get_order_name(order_code):
        """повертає назву клієнта по його коду

        Args:
            order_code ([type]): код клієнта

        Returns:
            [type]: назва клієнта
        """

        for dovidnyk in dovidnyks:
            if dovidnyk[0] == dovidnyk_code:
                return dovidnyk[1]

        return "*** код клієнта не знайдений"
    
    
    
    # накопичувач заявок 
    zajavka_list = []

    for dovidnyk in dovidnyks:
        
        # створити копію шаблона
        zajavka_tmp = zajavka.copy()

        zajavka_tmp['namet_name']    = dovidnyk[2]
        zajavka_tmp['kod_сlient']   = dovidnyk[1]
        zajavka_tmp['kol']            = dovidnyk[3]
        zajavka_tmp['price']          = dovidnyk[4]
        zajavka_tmp['total']          = zajavka_tmp['kol'] * zajavka_tmp['price']
        zajavka_tmp['order_number'] = get_client_name(dovidnyk[0])
=======
""" Заявки на продаж
"""

# Підключити функції з модуля 'data_service'
from data_service import get_order, get_dovidnik

# Структура заявок на продаж вихідних даних
zajavka = {
    'tovar_name'        : '',    # Назва товару 
    'number_order'      : 0,     # Номер заказа
    'code_client'       : '',    # Код клієнта
    'number'            : 0,     # Кількість
    'price'             : 0.0,     # Ціна
    'sum'               : 0.0,     # Сума
}


orders = get_order()
dovidniks = get_dovidnik()

def zajavka_sell():
    """ Формування заявок на продаж
    """

    def get_dovidnik_name(dovidnik_code):
        """ Повертає назву засоба по його коду

        Args:
            dovidnik_name ([type]): код засоба

        Returns:
            [type]: назва засобу
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_code:
                return dovidnik[1]

        return "*** Код засобу не знайдений"

    def get_dovidnik_price(dovidnik_price):
        """ Повертає назву засоба по його коду

        Args:
            dovidnik_price ([type]): код засоба

        Returns:
            [type]: назва засобу
        """

        for dovidnik in dovidniks:
            if dovidnik[0] == dovidnik_price:
                return dovidnik[2]

        return "*** Код засобу не знайдений"



    # Накопичувач заявок на продаж
    zajavka_list = []

    for order in orders:

        # Створити копію шаблона
        zajavka_tmp = zajavka.copy()

        zajavka_tmp['tovar_name'] = get_dovidnik_name(order[0])
        zajavka_tmp['number_order'] = order[1]
        zajavka_tmp['code_client'] = order[0]
        zajavka_tmp['number'] = order[3]
        zajavka_tmp['price'] = get_dovidnik_price(order[0])
        zajavka_tmp['sum'] = float(zajavka_tmp['number']) * float(zajavka_tmp['price'])
>>>>>>> main-module

        zajavka_list.append(zajavka_tmp)

    return zajavka_list

<<<<<<< HEAD
result = create_zajavka()

for r in result:
    print(r)

=======
result = zajavka_sell()

for r in result:
    print(r)
>>>>>>> main-module
