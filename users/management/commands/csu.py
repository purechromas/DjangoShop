from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='purechromaz@gmail.com',
            first_name='Благовест',
            last_name='Недков',
            is_active=True,
            is_staff=True,
            is_superuser=True,
            is_verified=True
        )

        user.set_password('admin')
        user.save()

