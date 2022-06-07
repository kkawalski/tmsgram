from django.db import models
from django.db.models import QuerySet
from django.db.models import Q, Value as V
from django.db.models.functions import Concat
from django.contrib.auth.models import AbstractUser, UserManager


class ProfileMixin(object):
    def users_without(self, user_id: int):
        return self.exclude(pk=user_id)

    def search(self, search=""):
        query = Q(username__icontains=search)
        query |= Q(fullname__icontains=search)
        return self.filter(query)


class ProfileQuerySet(QuerySet, ProfileMixin):
    pass


class ProfileManager(UserManager, ProfileMixin):
    def get_queryset(self):
        fullname = Concat("first_name", V(" "), "last_name") 
        return ProfileQuerySet(self.model, using=self._db).annotate(fullname=fullname)


class User(AbstractUser):
    following = models.ManyToManyField(
        "core.User", 
        related_name="followers",
        blank=True, null=True,
    )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    objects = ProfileManager()

    def __str__(self) -> str:
        return f"<User {self.username} {self.full_name}>"
