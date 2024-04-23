from django.core.management.base import BaseCommand, CommandError
from webhook.models import NamesMan, NamesWoman


class Command(BaseCommand):
    help = "Seeder for Man&Woman names"
    male_names = [
        "James", "John", "Robert", "Michael", "William",
        "David", "Richard", "Joseph", "Charles", "Thomas"
    ]

    female_names = [
        "Mary", "Patricia", "Jennifer", "Linda", "Elizabeth",
        "Barbara", "Susan", "Jessica", "Sarah", "Karen"
    ]

    def handle(self, *args, **options):
        print("Starting🏃 ...")

        male_objs = [NamesMan(name=name) for name in self.male_names]
        NamesMan.objects.bulk_create(male_objs)

        female_objs = [NamesWoman(name=name) for name in self.female_names]
        NamesWoman.objects.bulk_create(female_objs)

        print("Finished ✅")
