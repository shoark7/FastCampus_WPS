from django.db import models
from django.contrib.auth.models import \
    AbstractBaseUser, AbstractUser, \
    BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def create_superuser(
            self,
            email,
            last_name,
            first_name,
            nickname,
            password):
        user = self.model(
            email=email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname
        )
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user

    def create_user(
            self,
            email,
            last_name,
            first_name,
            nickname,
            password=None):
        user = self.model(
            email=email,
            last_name=last_name,
            first_name=first_name,
            nickname=nickname
        )
        user.set_password(password)
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=24, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('last_name', 'first_name', 'nickname', )

    objects = MyUserManager()

    def get_full_name(self):
        return '%s%s' % (self.last_name, self.first_name)

    def get_short_name(self):
        return self.first_name



