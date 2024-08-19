from typing import Any
from django.core.management import BaseCommand
from users.models import User

class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        if not User.objects.filter(email='admin@example.com').exists():
            admin = User.objects.create_superuser(
                email='admin@test.com',
                first_name='admin',
                last_name='admin',
                password='123qwe',
                phone='+79112345678',
            )
            self.stdout.write(self.style.SUCCESS('Суперпользователь успешно создан.'))
        else:
            self.stdout.write(self.style.WARNING('Суперпользователь с таким email уже существует.'))
