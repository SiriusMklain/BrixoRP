from django.shortcuts import render
from .models import *
from pathlib import Path



def app2(request):
    # 1 слайд.
    title = 'Итоги работы.'
    month = 'Декабрь'
    num_month = '5й месяц в Brixo'
    representative_name = 'Павел Головкин'
    job_title = 'Региональный Представитель:'
    location = 'Воронежская обл.'
    photo = ''

    # 2 слайд. Посещение ТТ
    title2 = 'Посещение ТТ:'
    tt_visits_in_month = '90'
    tt_visits_in_month_title = 'Визитов (ТТ) в этот месяц'
    tt_retail = '65'
    tt_retail_title = 'Розничных ТТ'
    sto = '25'
    sto_title = 'СТО'
    only_customer_order = '50%'
    only_customer_order_title = 'Не закупают SAKURA или только под заказ'
    dont_order = '30%'
    dont_order_title = 'Не закупают SAKURA или только под заказ'
    offer_and_sell = '20%'
    offer_and_sell_title = 'Предлагают и продают SAKURA'

    # 3 слайд. Предложения: что необходимо предпринять, чтобы увеличить долю присутствия SAKURA в ТТ:
    title3 = 'Предложения: что необходимо предпринять, чтобы увеличить долю присутствия SAKURA в ТТ:'
    paragraph1 = 'Внедрение практики проведения презентаций для ключевых клиентов, сетевых ТТ и дистрибьюторов.'
    paragraph2 = 'Организация и проведение семинаров совместно с  дистрибьюторами для ключевых и потенциальных клиентов.'
    paragraph3 = 'Необходимо присутствовать и представлять наши бренды на таких мероприятиях, как круглые столы от дистрибьюторов и др.'
    paragraph4 = 'Развитие маркетинга (например, акции для сетевых ТТ)'

    # 4 слайд. Сертификация ТТ:
    title41 = 'Сертификация ТТ:'
    certified_tt = '13'
    certified_tt_title = 'на 17.12.2023: Сертифицированных ТТ'
    certified_tt_percent = '33%'
    certified_tt_percent_title = '% выполнения квартального плана (40 ТТ)'

    dont_compliance_title = 'Причины отклонения/не выполнения (если есть):'
    dont_compliance = 'Основная причина – низкий объем продаж в ТТ, поэтому большинство не подходят под условия сертификации ввиду недостаточного количества закупок в течение необходимого периода (50 000 – 60 000 руб. по всем брендам в квартал).'

    # 4 слайд. Brixo bonus:
    title42 = 'Brixo bonus:'
    registered_inn = '1'
    registered_inn_title = 'зарегистрированных ИНН клиентов на 17.08.2023'

    invited_participate = '25'
    invited_participate_title = 'было предложено участие всего'
    refused = '10'
    refused_title = 'отказались, либо уже были зарегистрированы, либо не могут быть участниками (Дилеры)'

    customer_comments_title = 'Комментарии Клиентов/Обратная связь по brixo bonus:'
    customer_comments = 'Обратная связь положительная, так как многие клиенты соскучились по подобного рода акциям от производителей. На данный момент отказ получил только от 1 РТТ.'

    # 5 слайд. Акции/Мотивационные программы конкурентов:
    title5 = 'Акции/Мотивационные программы конкурентов'
    # таблица
    col51 = 'Бренд'
    col52 = 'Условия Акции/мотивационной программы, включая размеры премий, кэшбеков'


    # 6 слайд. Ценовая политика конкурентов VS. SAKURA:
    title61 = 'Ценовая политика конкурентов VS. SAKURA:'
    # таблица
    col61 = 'Бренд Конкурента'
    col62 = 'Артикул Конкурента'
    col63 = 'Цена конкурента'
    col64 = 'Наша Цена'
    col65 = 'Наш артикул'

    title62 = 'Рекламации/нарекания по нашим брендам:'
    # таблица
    coll61 = 'Наименование/Артикул/Применяемост'
    coll62 = 'Комментарии Клиента/от ТТ'
    title63 = 'Потенциальные Дилеры в городе/регионе:'
    # таблица
    colll61 = 'Количество'
    colll62 = 'Названия Розничных сетей'

    # 7 слайд. Общие комментарии по рынку (по работе)/замечания/предложения:
    title7 = 'Общие комментарии по рынку (по работе)/замечания/предложения:'
    comment = 'В целом, после посещения торговых точек, хотелось бы отметить, что доля ' \
              'присутствия наших торговых марок в ассортименте составляет не более 10%. ' \
              'В некоторых ТТ доступна только опция заказа нашей продукции после запроса ' \
              'клиента. В основном, покупатели останавливают свой выбор на нашей ТМ ввиду ' \
              'отсутствия альтернатив или благодаря приемлемой стоимости в сравнении с продукцией п' \
              'ремиум-сегмента. Во многих же ТТ наш бренд не представлен вовсе – ни в ассортименте, ' \
              'ни «под заказ». На данный момент, одной из приоритетных задач является работа со ' \
              'сложившимся стереотипом о том, что продукция Sakura ориентирована только на азиатские ' \
              'марки автомобилей. Большинству сотрудников ТТ не известно о нашей новой линейке продукции ' \
              'для европейских авто. Тем не менее, те ТТ, которые торгуют нашей продукцией, отмечают ' \
              'высокое качество брендов, большой ассортимент в наличии у дистрибьюторов на складах. ' \
              'Периодически поступают жалобы на стоимость, ввиду экономического кризиса, это довольно распространенное явление. '


    return render(request, 'app2/index.html')

