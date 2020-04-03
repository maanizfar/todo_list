from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('You have to provide a valid email address')

        if not username:
            raise ValueError('You have to provide a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        if not email:
            raise ValueError('You have to provide a valid email address.')

        if not username:
            raise ValueError('You have to provide a username.')

        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=60, unique=True, verbose_name='email')
    username = models.CharField(
        max_length=30, unique=True, verbose_name='username')
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name='date joined')
    last_login = models.DateTimeField(auto_now=True, verbose_name='last login')

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
