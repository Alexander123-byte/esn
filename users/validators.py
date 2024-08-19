from typing import Any
from rest_framework.exceptions import ValidationError


class NameValidator:
    def __init__(self, field) -> None:
        self.field = field

    def __call__(self, value, *args: Any, **kwargs: Any) -> Any:
        try:
            tmp_val = value[self.field]
        except:
            raise ValidationError('Ошибка имени')
        if type(tmp_val) is None:
            raise ValidationError('Имя не может быть пустым')
        if len(tmp_val) > 64:
            raise ValidationError('Имя слишком большое')