from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
import random


class Command(BaseCommand):
    help = 'Seed the database with sample listings and a user (idempotent)'

    def handle(self, *args, **options):
        User = get_user_model()
        host_username = 'host1'
        guest_username = 'guest1'

        host, _ = User.objects.get_or_create(username=host_username, defaults={'is_staff': False})
        guest, _ = User.objects.get_or_create(username=guest_username, defaults={'is_staff': False})

        sample_titles = [
            'Cozy Cottage',
            'Downtown Studio',
            'Beachside Bungalow',
            'Mountain Cabin',
            'Modern Apartment',
        ]

        created = 0
        for title in sample_titles:
            obj, created_flag = Listing.objects.get_or_create(
                title=title,
                defaults={
                    'description': f'Sample description for {title}',
                    'price': round(random.uniform(50, 300), 2),
                    'host': host,
                }
            )
            if created_flag:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Ensured users: {host.username}, {guest.username}'))
        self.stdout.write(self.style.SUCCESS(f'Created {created} new listings (or ensured existing).'))
