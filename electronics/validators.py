import datetime
from typing import Any
from rest_framework.exceptions import ValidationError


class ReleaseDateValidator:
    def __init__(self, field) -> None:
        self.field = field

    def __call__(self, value, *args: Any, **kwargs: Any) -> Any:
        try:
            tmp_val = value[self.field]
        except:
            raise ValidationError('Требуется дата выпуска')
        if type(tmp_val) is None:
            raise ValidationError('Дата выпуска не может быть пустой')
        tz = datetime.timezone('europe/Moscow')
        if tmp_val > datetime.datetime.now(tz):
            raise ValidationError('Дата релиза должна быть сегодняшней или раньше')


class SupplierValidator:
    def __init__(self, fields) -> None:
        self.supplier_choice = fields[0]
        self.factory = fields[1]
        self.network = fields[2]

    def __call__(self, value, *args: Any, **kwargs: Any) -> Any:
        tmp_choice = value[self.supplier_choice]
        tmp_factory = value[self.factory]
        tmp_network = value[self.network]
        if tmp_choice == 'ФАБРИКА' and (tmp_factory is None or tmp_network is not None):
            raise ValidationError('Поставщик должен быть после выбора поставщика (завод)')
        if tmp_choice == 'РОЗНИЧНАЯ СЕТЬ' and (tmp_network is None or tmp_factory is not None):
            raise ValidationError('Поставщик должен быть после выбора поставщика (сеть)')
