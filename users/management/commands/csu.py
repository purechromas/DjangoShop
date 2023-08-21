from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='superuser@gmail.com',
            first_name='superuser',
            is_active=True,
            is_verified=True,
            is_staff=True,
            is_superuser=True,
        )

        user.set_password('admin')
        user.save()

        user = User.objects.create(
            email='moderator@gmail.com',
            first_name='moderator',
            is_active=True,
            is_verified=True,
            is_staff=True,
            is_superuser=False,
        )

        user.set_password('admin')
        user.save()

        user = User.objects.create(
            email='user@gmail.com',
            first_name='user',
            is_active=True,
            is_verified=True,
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('admin')
        user.save()

        user = User.objects.create(
            email='user1@gmail.com',
            first_name='user',
            is_active=True,
            is_verified=True,
            is_staff=False,
            is_superuser=False,
        )

        user.set_password('admin')
        user.save()
