from django import template
from django.db.models import QuerySet

register = template.Library()


@register.filter
def split(value, delimiter):
    return value.split(delimiter)


@register.filter
def format_price(value):
    """Форматирует цену с пробелами между тысячами"""
    try:
        # Убираем десятичные нули и форматируем
        number = int(value) if value % 1 == 0 else float(value)
        return "{:,}".format(number).replace(",", " ") + " руб."
    except:
        return "Цена не указана"


@register.filter
def format_price_2(value):
    """Форматирует цену с пробелами между тысячами"""
    try:
        # Убираем десятичные нули и форматируем
        number = int(value) if value % 1 == 0 else float(value)
        return "{:,}".format(number).replace(",", " ")
    except:
        return "Цена не указана"


@register.filter
def format_weight(value):
    try:
        # Убираем десятичные нули и форматируем
        number = int(value) if value % 1 == 0 else float(value)
        return number
    except:
        return "Цена не указана"


@register.filter
def truncate_transmission(value):
    """Обрезает значение трансмиссии до 3 символов"""
    return value[:3].upper() if len(value) > 3 else value


@register.filter
def filter_services(services, car_id):
    return [s for s in services if s.car_camping.id == car_id]


@register.filter
def sum_prices(items):
    try:
        if isinstance(items, QuerySet) or isinstance(items, list):
            return sum(float(item.service.price) for item in items)
        return 0
    except Exception as e:
        print(f"Error in sum_prices: {e}")
        return 0

