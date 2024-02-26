from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, usr_username, usr_email, usr_password=None):
        if not usr_username:
            raise ValueError('Users must have a username')
        if not usr_email:
            raise ValueError('Users must have an email address')

        user = self.model(
            usr_username=usr_username,
            usr_email=self.normalize_email(usr_email),
        )

        user.set_password(usr_password)
        user.save(using=self._db)
        return user

    def create_superuser(self, usr_username, usr_email, usr_password):
        user = self.create_user(
            usr_username,
            usr_email,
            usr_password,
        )
        user.usr_is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    usr_username = models.CharField(max_length=100, unique=True)
    usr_email = models.EmailField(unique=True)
    usr_created_at = models.DateTimeField(auto_now_add=True)
    usr_updated_at = models.DateTimeField(auto_now=True)
    usr_is_active = models.BooleanField(default=True)
    usr_is_admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'usuario'

    objects = UserManager()

    USERNAME_FIELD = 'usr_username'
    REQUIRED_FIELDS = ['usr_email']

    def __str__(self):
        return self.usr_username

    def has_perm(self, perm, obj=None):
        return self.usr_is_admin

    def has_module_perms(self, app_label):
        return self.usr_is_admin
