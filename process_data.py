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

        zajavka_list.append(zajavka_tmp)

    return zajavka_list

result = create_zajavka()

for r in result:
    print(r)

