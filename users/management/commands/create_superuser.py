from django.core.management import BaseCommand
from users.models import User, UserRoles


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="admin@mail.ru",
            first_name="admin",
            last_name="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True,
            role=UserRoles.MODERATOR
            )

        user.set_password("12345")
        user.save()

        user = User.objects.create(
            email="test@mail.ru",
            first_name="test",
            last_name="test",
            is_superuser=False,
            is_staff=False,
            is_active=True,
            role=UserRoles.MEMBER
        )

        user.set_password("12345")
        user.save()

        user = User.objects.create(
            email="test2@mail.ru",
            first_name="test2",
            last_name="test2",
            is_superuser=False,
            is_staff=False,
            is_active=True,
            role=UserRoles.MEMBER
        )

        user.set_password("12345")
        user.save()

        user = User.objects.create(
            email="test3@mail.ru",
            first_name="test3",
            last_name="test3",
            is_superuser=False,
            is_staff=False,
            is_active=True,
            role=UserRoles.MEMBER
        )

        user.set_password("12345")
        user.save()

        user = User.objects.create(
            email="moderator@mail.ru",
            first_name="moderator",
            last_name="moderator",
            is_superuser=False,
            is_staff=True,
            is_active=True,
            role=UserRoles.MODERATOR
        )

        user.set_password("12345")
        user.save()