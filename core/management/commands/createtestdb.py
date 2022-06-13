import random

from django.core.management.base import BaseCommand

from core.models import User
from posts.models import Post, HashTag

usernames = ["test", "user", "dummy"]
posts = ["description", "test", "dummy", "#tag", "#lol", "#mem"]


class Command(BaseCommand):
    help = "Init test data"

    def handle(self, *args, **options):
        for i in random.randint(3, 6):
            user = User(username=f"{random.choice(usernames)}{i}")

