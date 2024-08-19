from typing import Any
from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        admin = User.objects.create(
            email='admin@example.com',
            first_name='admin',
            last_name='admin',
            is_staff=True,
            is_superuser=True,
            phone='+79112345678',
        )
        admin.set_password('123qwe')
        admin.save()
