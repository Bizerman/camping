from profile import Profile

from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from camping_back.camping_bd.models import CarCamping, OrderCarCamping, Order, Tent, AdditionalService, \
    OrderAdditionalService, OrderTent
from django.contrib.auth.models import User

def check_auth(request):
    auth_user = request.user
    if auth_user.is_authenticated:
        user = User.objects.get(id=auth_user.id)
        return user
    else:
        return None
def logout_user(request):
    logout(request)
    return main_page_render(request)
def car_campings_page_render(request):
    order = get_draft_order(request.user) if request.user.is_authenticated else None
    total_quantity = order.get_quantity() if order else 0
    search_query = request.GET.get('car_camping', '').strip().lower()
    sort_order = request.GET.get('sort', 'desc')
    cars = CarCamping.objects.prefetch_related('images').all()
    if search_query:
        cars = cars.filter(title__icontains=search_query)
    auth_user = check_auth(request)
    if sort_order == 'asc':
        cars = cars.order_by('price')
        next_sort = 'desc'
    else:
        cars = cars.order_by('-price')
        next_sort = 'asc'
    return render(request, 'car_campings.html', {
        'auth':auth_user,
        'data': {
            'car_camping': cars,
            'order': order,
            'quantity': total_quantity,
            'search': search_query
        },
        'sort_order': next_sort
    })


def car_camping_page_render(request, id):
    order = get_draft_order(request.user) if request.user.is_authenticated else None
    total_quantity = order.get_quantity() if order else 0
    product = get_object_or_404(CarCamping, id=id)
    services = AdditionalService.objects.all()
    add_service_url = reverse('add_service_to_order', args=[0, id])
    specs = [
        {'name': 'Д/Ш/В, мм', 'value': f"{product.length} / {product.width} / {product.height}"},
        {'name': 'Коробка передач', 'value': product.transmission},
        {'name': 'Двигатель', 'value': product.engine},
        {'name': 'Категория', 'value': product.category},
        {'name': 'Шасси', 'value': product.chassis},
        {'name': 'Топливный бак', 'value': f"{product.fuel_tank}л дизель"},

        # Системы безопасности и комфорт
        {'name': 'ABS, EBD, ASR', 'type': 'bool', 'value': product.safety_features},
        {'name': 'Гидроусилитель руля', 'type': 'bool', 'value': product.steering},
        {'name': 'Круиз контроль', 'type': 'bool', 'value': product.cruise_control},
        {'name': 'Магнитола 2din с камерой', 'type': 'bool', 'value': product.multimedia},
        {'name': 'Кабинный кондиционер', 'type': 'bool', 'value': product.conditioner},
        {'name': 'Бортовой компьютер', 'type': 'bool', 'value': product.computer},

        # Спальные места
        {'name': 'Ремней безопасности', 'value': product.seatbelts},
        {'name': 'Спальные места', 'value': product.seats},
        {'name': 'Задняя кровать, мм', 'value': f"2 * {product.alcov_sleeper_length}×{product.alcov_sleeper_width}"},
        {'name': 'Кровать в алькове, мм', 'value': f"{product.alcov_sleeper_length}×{product.alcov_sleeper_width}"},
        {'name': 'Доп. спальное место, мм',
         'value': f"{product.additional_sleeper_length}×{product.additional_sleeper_width}"},

        # Кухня и водоснабжение
        {'name': 'Холодильник', 'value': f"{product.fridge} с морозильным отсеком"},
        {'name': 'Столовая группа (чел.)', 'value': product.dining_group},
        {'name': 'Водоснабжение, л', 'value': f"{product.water_system}"},
        {'name': 'Газ. плита с раковиной', 'type': 'bool', 'value': product.kitchen_equipment},

        # Дополнительное оборудование
        {'name': 'Маркиза, м', 'value': product.awning},
        {'name': 'Велобагажник', 'value': f"{product.bike_rack} велосипеда"},
        {'name': 'Окна с сетками', 'type': 'bool', 'value': product.windows},
        {'name': 'Внутр. высота, мм', 'value': product.internal_height}
    ]
    auth_user = check_auth(request)
    return render(request, 'car_camping.html', {
        'auth': auth_user,
        'product': product,
        'specs': specs,
        'services': services,
        'add_service_url': add_service_url,
        'data':{
            'order' : order,
            'quantity': total_quantity,
        }
    })

def tents_page_render(request):
    order = get_draft_order(request.user) if request.user.is_authenticated else None
    total_quantity = order.get_quantity() if order else 0
    search_query = request.GET.get('tents', '').strip().lower()
    tents = Tent.objects.prefetch_related('images').all()
    sort_order = request.GET.get('sort', 'desc')
    auth_user = check_auth(request)
    if search_query:
        tents = tents.filter(name__icontains=search_query)
    if sort_order == 'asc':
        tents = tents.order_by('price')
        next_sort = 'desc'
    else:
        tents = tents.order_by('-price')
        next_sort = 'asc'
    return render(request, 'tents_page.html', {
        'auth': auth_user,
        'data': {
            'tents': tents,
            'order': order,
            'quantity': total_quantity,
            'search': search_query
        },
        'sort_order': next_sort
    })
def tent_page_render(request, id):
    order = get_draft_order(request.user) if request.user.is_authenticated else None
    total_quantity = order.get_quantity() if order else 0
    product = get_object_or_404(
        Tent.objects.prefetch_related('images'),
        id=id
    )

    specs = [
        # Основные характеристики
        {'name': 'Назначение', 'value': product.purpose},
        {'name': 'Количество мест', 'value': product.capacity},
        {'name': 'Вес', 'value': f"{product.weight} кг"},

        # Конструкция
        {'name': 'Тип каркаса', 'value': product.frame_type},
        {'name': 'Геометрия', 'value': product.geometry},
        {'name': 'Внутренняя палатка', 'type': 'bool', 'value': product.inner_tent},
        {'name': 'Быстрая сборка', 'type': 'bool', 'value': product.quick_assembly},

        # Элементы конструкции
        {'name': 'Количество входов', 'value': product.entries},
        {'name': 'Количество тамбуров', 'value': product.vestibules},
        {'name': 'Количество комнат', 'value': product.rooms},
        {'name': 'Ветрозащитная юбка', 'type': 'bool', 'value': product.snowskirt},
        {'name': 'Окна', 'type': 'bool', 'value': product.windows},

        # Дополнительные особенности
        {'name': 'Штормовые оттяжки', 'type': 'bool', 'value': product.storm_guys},
        {'name': 'Внутренние карманы', 'type': 'bool', 'value': product.inner_pockets},
        {'name': 'Противомоскитная сетка', 'type': 'bool', 'value': product.mosquito_net},
        {'name': 'Огнеупорная пропитка', 'type': 'bool', 'value': product.fireproof},
        {'name': 'Герметизация швов', 'value': product.seam_sealing},

        # Материалы
        {'name': 'Материал тента', 'value': f"{product.tent_material} ({product.tent_waterproof} мм в.ст.)"},
        {'name': 'Материал дна', 'value': f"{product.floor_material} ({product.floor_waterproof} мм в.ст.)"},
        {'name': 'Материал дуг', 'value': product.pole_material},

        # Размеры
        {'name': 'Внешние размеры', 'value': product.external_dimensions},
        {'name': 'Внутренние размеры', 'value': product.internal_dimensions if product.internal_length else "Н/Д"},
        {'name': 'Размеры в упаковке', 'value': product.packed_dimensions},
    ]
    auth_user = check_auth(request)
    return render(request, 'tent_page.html', {
        'auth' : auth_user,
        'product': product,
        'specs': specs,
        'data': {
            'quantity': total_quantity,
            'order': order,
        }
    })


def order_page_render(request, id):
    auth_user = check_auth(request)
    order = get_object_or_404(Order, pk=id)
    total_quantity = order.get_quantity() if order else 0

    if order.status == 5:
        return render(request, "404.html")

    # Получаем все связанные объекты
    cars = order.car_camping_items.select_related('car_camping')
    tents = order.tent_items.select_related('tent')
    services = order.service_items.select_related('service', 'car_camping')

    # Собираем данные для шаблона
    context = {
        'auth': auth_user,
        'cars': [item.car_camping for item in cars],
        'tents': [item.tent for item in tents],
        'services': services,
        'data': {
            'quantity': total_quantity,
            'order': order,
        }
    }

    return render(request, 'order.html', context)
def main_page_render(request):
    auth_user = check_auth(request)
    order = get_draft_order(request.user) if request.user.is_authenticated else None
    total_quantity = order.get_quantity() if order else 0
    return render(request, 'main_page.html',
                  {'auth' : auth_user,
                   'data':
                       {'quantity': total_quantity,
                        'order': order,
                        }})


def login_page_render(request):
    error = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Используем кастомный бэкенд для аутентификации по email
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('main_page_url')
        else:
            error = "Неверный email или пароль"

    return render(request, 'login_page.html', {'error': error})


def sign_up_page_render(request):
    error = None
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists():
                error = "Пользователь с таким именем уже существует"
            elif User.objects.filter(email=email).exists():
                error = "Пользователь с таким email уже существует"
            else:
                user = User.objects.create_user(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    password=password
                )
                user.save()
                return redirect('login_url')  # Замените 'login' на имя вашего маршрута входа

        except Exception as e:
            error = f"Ошибка при регистрации: {str(e)}"

    return render(request, 'sign_up_page.html', {'error': error})


def add_to_order(request, product_type, product_id):
    if not request.user.is_authenticated:
        return redirect('login_url')

    PRODUCT_MAPPING = {
        'car_camping': (CarCamping, OrderCarCamping),
        'tent': (Tent, OrderTent),
    }

    if product_type not in PRODUCT_MAPPING:
        return render(request, "404.html")

    model_class, order_model = PRODUCT_MAPPING[product_type]

    # Получаем продукт
    product = get_object_or_404(model_class, id=product_id)
    user = request.user

    # Получаем или создаем черновик заказа (статус=1)
    draft_order, created = Order.objects.get_or_create(
        status=1,
        creator=user,
        defaults={
            'total_price': 0,
            'create_datetime': timezone.now()
        }
    )

    # Проверяем, не добавлен ли уже продукт в заказ
    if not order_model.objects.filter(order=draft_order, **{f'{product_type}': product}).exists():
        # Создаем связь через промежуточную модель
        order_model.objects.create(
            order=draft_order,
            **{f'{product_type}': product},
            price=product.price
        )

        # Обновляем общую сумму заказа
        draft_order.total_price += product.price
        draft_order.save()

    # Редирект на страницу продукта
    REDIRECT_MAPPING = {
        'car_camping': 'car_camping_url',
        'tent': 'tent_url',
    }
    return redirect(REDIRECT_MAPPING[product_type], id=product_id)
def add_service_to_order(request, service_id, car_id):
    print("Функция add_service_to_order вызвана!")  # Проверка
    print(f"Service ID: {service_id}, Car ID: {car_id}")  # Вывод параметров
    if not request.user.is_authenticated:
        return redirect('login_url')
    print(service_id, car_id)
    service = get_object_or_404(AdditionalService, id=service_id)
    car_camping = get_object_or_404(CarCamping, id=car_id)
    user = request.user

    # Получаем/создаем черновик заказа
    draft_order, created = Order.objects.get_or_create(
        status=1,
        creator=user,
        defaults={'total_price': 0, 'create_datetime': timezone.now()}
    )

    # Проверяем, не добавлена ли уже услуга для этого авто
    if not OrderAdditionalService.objects.filter(
        order=draft_order,
        service=service,
        car_camping=car_camping
    ).exists():
        OrderAdditionalService.objects.create(
            order=draft_order,
            service=service,
            car_camping=car_camping,
            price=service.price
        )
        draft_order.total_price += service.price
        draft_order.save()

    return redirect('car_camping_url', id=car_id)
def del_order(request,id):
    if not Order.objects.filter(pk=id).exists():
        return redirect("/")
    with connection.cursor() as cursor:
        cursor.execute("UPDATE orders SET status=5 WHERE id=%s",[id])
    return redirect("/")
def get_draft_order(user):
    if user.is_authenticated:
        return Order.objects.filter(
            status=1,
            creator=user
        ).prefetch_related(
            'car_camping_items',
            'tent_items',
            'service_items'
        ).first()
    return None


def get_current_user():
    return User.objects.filter().first()


def finalize_order(request, id):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=id)
        order.status = 2
        order.save()
    return redirect('main_page_url')