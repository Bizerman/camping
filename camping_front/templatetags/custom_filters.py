from django import template

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
def truncate_transmission(value):
    """Обрезает значение трансмиссии до 3 символов"""
    return value[:3].upper() if len(value) > 3 else value
