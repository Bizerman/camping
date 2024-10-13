from django.shortcuts import render
products = [{'id': 1,
             'title': 'Cygnus',
             'description': 'Автономный грузовой космический корабль одноразового использования.',
             'image':'http://127.0.0.1:9000/img-for-rip/images/',
             'info':'Cygnus состоит из двух основных компонентов: сервисного модуля и грузового отсека. Сервисный модуль содержит двигатели, топливные баки, систему управления и другие системы, необходимые для управления полётом корабля. Грузовой отсек предназначен для перевозки различных грузов, таких как продукты питания, научное оборудование, материалы для экспериментов и т. д.\n'
                    'Корабль запускается с помощью ракеты-носителя Antares, которая выводит его на орбиту. После отделения от ракеты-носителя Cygnus использует свои двигатели для корректировки орбиты и сближения с Международной космической станцией. Стыковка с МКС осуществляется с помощью манипулятора Canadarm2, который захватывает корабль и подводит его к стыковочному узлу станции.\n'
                    'После разгрузки груза Cygnus может быть использован для проведения экспериментов или для возвращения грузов с МКС на Землю. Для этого корабль отделяется от станции и возвращается в атмосферу Земли, где его грузовой отсек сгорает, а оставшиеся части падают в океан.\n'
             },
            {'id': 2,
            'title': 'Power and Propulsion Element (PPE)',
             'description': 'Модуль будет обеспечивать станцию Gateway энергией и управлять её двигательной установкой.',
             'image':'http://127.0.0.1:9000/img-for-rip/images/',
             'info':''},
            {'id': 3,
             'title': 'Dragon Crew Spacecraft',
             'description': 'Автономный космический корабль, предназначенный для доставки экипажа и критически важных грузов на орбиту.',
             'image':'http://127.0.0.1:9000/img-for-rip/images/',
             'info' : 'Размеры - S-XXL\n'
                      'Состав - Хлопок 60% / Полиэстр 40%'},
            {'id': 4,
             'title': 'Habitation and Logistics Outpost (HALO)',
             'description': 'Жилой модуль , который обеспечит астронавтов рабочим пространством для исследования Луны и проживания на станции',
             'image':'http://127.0.0.1:9000/img-for-rip/images/',
             'info': 'Размеры - S-XXL\n'
                     'Состав - Хлопок 60% / Полиэстр 40%'},
            {'id': 5,
             'title': 'Starliner Crew Spacecraft',
             'description': 'Коммерческий космический корабль компании Boeing для перевозки людей.',
             'image':'http://127.0.0.1:9000/img-for-rip/images/',
             'info' : 'Размеры - S-XXL\n'
                      'Состав - Хлопок 60% / Полиэстр 40%'},
            {'id': 6,
             'title': 'Dragon Cargo Spacecraft',
             'description': 'Доставляет грузы на МКС и способен возвращать грузы обратно на Землю.',
             'image':'http://127.0.0.1:9000/img-for-rip/images/',
             'info' : 'Размеры - S-XXL\n'
                      'Состав - Хлопок 60% / Полиэстр 40%'},]
orders = [{'id': 1,
               'products': [{'id': 2,'title': 'Power and Propulsion Element (PPE)',
             'description': 'Модуль будет обеспечивать станцию Gateway энергией и управлять её двигательной установкой.',
             'image':'http://127.0.0.1:9000/img-for-rip/images/',
             'info':''},{'id': 4,'title': 'Habitation and Logistics Outpost (HALO)',
             'description': 'Жилой модуль , который обеспечит астронавтов рабочим пространством для исследования Луны и проживания на станции',
             'image':'http://127.0.0.1:9000/img-for-rip/images/',
             'info': 'Размеры - S-XXL\n'
                     'Состав - Хлопок 60% / Полиэстр 40%'}],
               'quantity': 2}]

def main_page_render(request):
    order = next((item for item in orders if item['id'] == 1), None)
    search_query = request.GET.get('gateway_el', '')
    filtered_products = [
        product for product in products
        if search_query in product['title']
    ]
    return render(request, 'products.html', {'data' : {'products' : filtered_products, 'order' : order, 'search':search_query}})
def product_page_render(request,id):
    product = next((item for item in products if item['id'] == id), None)
    return render(request, 'product.html',{'product': product})
def cart_page_render(request, id):
    order = next((item for item in orders if item['id'] == id), None)
    return render(request, 'orders.html', {'order': order})

