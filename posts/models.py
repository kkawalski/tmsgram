import os
from django.conf import settings
from django.db import models
from django.db.models import QuerySet, Q

from core.models import TimeStampMixin, User


class PostMixin(object):
    def following(self, user: User):
        query = models.Q(user__in=user.following.all())
        query |= models.Q(user=user)
        return self.filter(query)

class PostQuerySet(QuerySet, PostMixin):
    pass


class PostManager(models.Manager, PostMixin):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)


def upload_to_user_dir(instance, filename):
    return os.path.join(instance.user.username, filename)


class Post(TimeStampMixin):
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to=upload_to_user_dir, blank=True, null=True)
    user = models.ForeignKey(
        "core.User", 
        on_delete=models.CASCADE,
        related_name="posts",
        blank=False, null=False,
    )

    objects = PostManager()

    def __str__(self) -> str:
        return f"Post {self.id} by user {self.user}"

    class Meta:
        ordering = ("-created_at", "-id")
