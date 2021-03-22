from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    # username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    mid_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(_("email address"), unique=True)
    phone = models.CharField(max_length=15, blank=True)
    dob = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    # Link Manager.py 
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []


    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
         return CustomUser.objects.get(email=email)
        except:
            False

    def isExixts(self):
        if CustomUser.objects.filter(email = self.email):
            return True
        return False














# from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import ugettext_lazy as _
# from .managers import CustomUserManager
# # Create your models here.
# class CustomUser(AbstractUser):
#     username = None
#     email = models.EmailField(_("email address"), unique=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELD = []
#     objects = CustomUserManager()
#     def __str__(self):
#         return self.email
        