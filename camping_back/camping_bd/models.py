
from django.contrib.auth.models import User
from django import forms

# Create your models here.
from django.db import models
from django.utils import timezone


class CarCamping(models.Model):
    # Основная информация
    title = models.CharField(max_length=200, verbose_name="Название модели")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        default=0.00
    )
    short_description = models.TextField(verbose_name="Краткое описание")
    description = models.TextField(verbose_name="Описание")

    # Габариты
    length = models.IntegerField(verbose_name="Длина (мм)")
    width = models.IntegerField(verbose_name="Ширина (мм)")
    height = models.IntegerField(verbose_name="Высота (мм)")
    internal_height = models.IntegerField(verbose_name="Внутренняя высота (мм)")

    # Трансмиссия и двигатель
    transmission = models.CharField(max_length=50, verbose_name="Коробка передач")
    engine = models.CharField(max_length=100, verbose_name="Двигатель")
    fuel_tank = models.IntegerField(verbose_name="Объем топливного бака (л)")

    # Безопасность
    safety_features = models.TextField(
        verbose_name="Системы безопасности",
        help_text="ABS, EBD, ASR и другие системы"
    )

    # Комфорт
    steering = models.BooleanField(default=False,max_length=100, verbose_name="Гидроусилитель руля")
    cruise_control = models.BooleanField(default=False, verbose_name="Круиз контроль")
    conditioner = models.BooleanField(default=False, verbose_name="Кондиционер")
    multimedia = models.BooleanField(default=False,verbose_name="Магнитола 2din с камерой заднего вида")

    # Спальные места
    seats = models.IntegerField(verbose_name="Количество мест")
    seatbelts = models.IntegerField(verbose_name="Ремней безопасности")
    alcov_sleeper_length = models.IntegerField(verbose_name="Кровать в алькове (длина), мм")
    alcov_sleeper_width = models.IntegerField(verbose_name="Кровать в алькове (ширина), мм")
    additional_sleeper_length = models.IntegerField(verbose_name="Столовая группа трансформируется в дополнительное спальное место (длина), мм")
    additional_sleeper_width = models.IntegerField(
        verbose_name="Столовая группа трансформируется в дополнительное спальное место (ширина), мм")

    # Кухня
    kitchen_equipment = models.BooleanField(
        verbose_name="Раковина из нержавеющей стали и З-х конфорочная газ. плита",
        help_text="Раковина, плита и т.д."
    )
    dining_group = models.IntegerField(verbose_name="Столовая группа до (чел.)")

    # Водоснабжение
    water_system = models.IntegerField(verbose_name="Запас воды/объем бака сточной воды, л")

    # Дополнительное оборудование
    awning = models.IntegerField(verbose_name="Маркиза механическая, м")
    bike_rack = models.IntegerField(verbose_name="Велобагажник(вел.)")

    # Технические характеристики
    chassis = models.CharField(max_length=100, verbose_name="Шасси")
    category = models.CharField(max_length=50, verbose_name="Категория ТС")

    # Хранение
    fridge = models.CharField(max_length=100, verbose_name="Холодильник, л")
    freezer = models.CharField(max_length=100, verbose_name="Отдельная морозильная камера, л")

    # Дополнительная информация
    windows = models.BooleanField(verbose_name="Окна жилого модуля со шторами и москитными сетками")
    computer = models.BooleanField(default=True, verbose_name="Бортовой компьютер")


    class Meta:
        verbose_name = "Кемпинг-автомобиль"
        verbose_name_plural = "Кемпинг-автомобили"


class CarCampingImage(models.Model):
    car = models.ForeignKey(
        CarCamping,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        upload_to='car_camping/',
        verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Изображение кемпинг-автомобиля"
        verbose_name_plural = "Изображения кемпинг-автомобилей"
class AdditionalService(models.Model):

    name = models.CharField(max_length=200, verbose_name="Название услуги")
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name="Стоимость"
    )
    class Meta:
        verbose_name = "Дополнительная услуга"
        verbose_name_plural = "Дополнительные услуги"
        ordering = ['name']


class Tent(models.Model):
    # Основные характеристики
    name = models.CharField(max_length=200, verbose_name="Название модели")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
        default=0.00
    )
    description = models.TextField(verbose_name="Описание")
    capacity = models.IntegerField(verbose_name="Количество мест")
    purpose = models.CharField(max_length=50, default="кемпинговая", verbose_name="Назначение")

    # Конструкция
    frame_type = models.CharField(max_length=50, verbose_name="Тип каркаса")
    geometry = models.CharField(max_length=50, verbose_name="Геометрия")
    inner_tent = models.BooleanField(default=True, verbose_name="Внутренняя палатка")
    quick_assembly = models.BooleanField(default=False, verbose_name="Быстрая сборка")

    # Элементы конструкции
    entries = models.IntegerField(verbose_name="Количество входов")
    vestibules = models.IntegerField(verbose_name="Количество тамбуров")
    rooms = models.IntegerField(verbose_name="Количество комнат")
    snowskirt = models.BooleanField(default=False, verbose_name="Ветрозащитная юбка")
    windows = models.BooleanField(default=False, verbose_name="Окна")

    # Дополнительные особенности
    storm_guys = models.BooleanField(default=True, verbose_name="Штормовые оттяжки")
    inner_pockets = models.BooleanField(default=True, verbose_name="Внутренние карманы")
    mosquito_net = models.BooleanField(default=True, verbose_name="Противомоскитная сетка")
    fireproof = models.BooleanField(default=False, verbose_name="Огнеупорная пропитка")
    seam_sealing = models.CharField(max_length=50, verbose_name="Герметизация швов")

    # Материалы
    tent_material = models.CharField(max_length=100, verbose_name="Материал тента")
    floor_material = models.CharField(max_length=100, verbose_name="Материал дна")
    inner_material = models.CharField(max_length=100, verbose_name="Материал внутренней палатки")
    pole_material = models.CharField(max_length=100, verbose_name="Материал дуг")
    tent_waterproof = models.IntegerField(verbose_name="Водостойкость тента (мм в.ст.)", default=0)
    floor_waterproof = models.IntegerField(verbose_name="Водостойкость дна (мм в.ст.)", default=0)

    # Размеры и вес
    external_length = models.IntegerField(verbose_name="Длина (см)")
    external_width = models.IntegerField(verbose_name="Ширина (см)")
    external_height = models.IntegerField(verbose_name="Высота (см)")
    internal_length = models.IntegerField(verbose_name="Внутренняя длина (см)", default=0)
    internal_width = models.IntegerField(verbose_name="Внутренняя ширина (см)", default=0)
    internal_height = models.IntegerField(verbose_name="Внутренняя высота (см)", default=0)
    packed_length = models.IntegerField(verbose_name="Длина упаковки (см)")
    packed_width = models.IntegerField(verbose_name="Ширина упаковки (см)")
    packed_height = models.IntegerField(verbose_name="Высота упаковки (см)")
    weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Вес (кг)")



    class Meta:
        verbose_name = "Палатка"
        verbose_name_plural = "Палатки"
        ordering = ['name']
        db_table = 'tents'

    def __str__(self):
        return f"{self.name} ({self.capacity} мест)"

    @property
    def external_dimensions(self):
        return f"{self.external_length}x{self.external_width}x{self.external_height} см"

    @property
    def internal_dimensions(self):
        return f"{self.internal_length}x{self.internal_width}x{self.internal_height} см"

    @property
    def packed_dimensions(self):
        return f"{self.packed_length}x{self.packed_width}x{self.packed_height} см"


class TentImage(models.Model):
    tent = models.ForeignKey(
        Tent,
        on_delete=models.CASCADE,
        related_name='images'
    )
    image = models.ImageField(
        upload_to='tents/',
        verbose_name="Изображение"
    )

    class Meta:
        verbose_name = "Изображение палатки"
        verbose_name_plural = "Изображения палаток"


class Order(models.Model):
    STATUS_CHOICES = (
        (1, 'Создан'),
        (2, 'Оплачен'),
        (3, 'Завершен'),
        (4, 'Отменен'),
    )

    creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Создатель",
        null=True
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name="Статус")
    create_datetime = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая стоимость")
    complete_datetime = models.DateTimeField(null=True, blank=True, verbose_name="Дата завершения")

    car_campings = models.ManyToManyField(CarCamping, through='OrderCarCamping', related_name='orders')
    tents_list = models.ManyToManyField(Tent, through='OrderTent', related_name='orders')
    services = models.ManyToManyField(AdditionalService, through='OrderAdditionalService',related_name='orders')
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ('-create_datetime',)
        db_table = 'orders'

    def get_quantity(self):
        return (
            self.car_camping_items.count() +
            self.tent_items.count() +
            self.service_items.count()
        )

class OrderCarCamping(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='car_camping_items')
    car_camping = models.ForeignKey(CarCamping, on_delete=models.PROTECT, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена на момент заказа")

    class Meta:
        db_table = 'order_car_campings'
        constraints = [
            models.UniqueConstraint(fields=['order', 'car_camping'], name="order_car_camping_unique")
        ]


class OrderTent(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tent_items')
    tent = models.ForeignKey(Tent, on_delete=models.PROTECT, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена на момент заказа")

    class Meta:
        db_table = 'order_tents'
        constraints = [
            models.UniqueConstraint(fields=['order', 'tent'], name="order_tent_unique")
        ]

class OrderAdditionalService(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='service_items')
    service = models.ForeignKey(AdditionalService, on_delete=models.PROTECT, related_name='order_service')
    car_camping = models.ForeignKey(  # Добавляем связь с автомобилем
        CarCamping,
        default=0,
        on_delete=models.PROTECT,
        related_name='additional_services',
        verbose_name="Связанный автомобиль",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена на момент заказа")

    class Meta:
        db_table = 'order_additional_services'
        constraints = [
            models.UniqueConstraint(
                fields=['order', 'service', 'car_camping'],
                name="order_service_car_unique"
            )
        ]
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, max_length=32, label="Password")
    repeat_password = forms.CharField(widget=forms.PasswordInput, max_length=32, label="Repeat password")
    nickname = forms.CharField(max_length=32, required=True, label="Nickname")
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeat_password = cleaned_data.get('repeat_password')

        if password != repeat_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data