from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password, **kwargs):
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(force_insert=True, using=self.db)
        return user

    def create_superuser(self, username, password):
        return self.create_user(username, password, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'

    username = models.CharField(max_length=20, unique=True)
    is_superuser = models.BooleanField(default=False)

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self):
        return self.username

    objects = UserManager()
