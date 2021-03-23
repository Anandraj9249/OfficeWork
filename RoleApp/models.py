from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _
# from multiselectfield import MultiSelectField

# Create your models here.
# class UserType(models.Model):
#     ADMIN = 1
#     SUB_ADMIN = 2
#     USER = 3
#     TYPE_CHOICES = (
#         (USER , 'User'),
#         (SUB_ADMIN , 'Sub_Admin'),
#         (ADMIN , 'Admin') 
#     )
#     id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True, default= USER)
#     def __str__(self):
#         return self.get_id_display()


# class Countries(models.Model):
#     Cname = models.CharField(max_length=100)

# class States(models.Model):
#     Cname = models.ForeignKey(Countries, on_delete=models.CASCADE)
#     Sname  = models.CharField(max_length=100)

# class Cities(models.Model):
#     Cname = models.ForeignKey(Countries, on_delete=models.CASCADE)
#     Sname = models.ForeignKey(States, on_delete=models.CASCADE)
#     cityName = models.CharField(max_length=100)

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
    # address = models.CharField(max_length=500)
    Cname = models.CharField(max_length=100)
    Sname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    class Types(models.TextChoices):
            ADMIN = "Admin", "ADMIN"
            SUB_ADMIN = "Sub_admin", "SUB_ADMIN"
            USER = "User", "USER"
    default_type = Types.USER
    type = models.CharField(_('Type') , max_length=255, choices=Types.choices, default=default_type)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
    
    # Link Manager.py 
    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.default_type
            # self.type.append(self.default_type)
        return super().save(*args, **kwargs)

    def register(self):
        self.save()

    @staticmethod
    def get_user_by_email(email):
        try:
         return CustomUser.objects.get(email=email)
        except:
            False

    def isExist(self):
        if CustomUser.objects.filter(email = self.email):
            return True
        return False
    #User Filters by id
    @staticmethod
    def get_all_users_by_id(user_id):
        if user_id:   
            return CustomUser.objects.filter(user = user_id)
        else:
            return CustomUser.objects.all()

# add extra field 
class AdminAdditional(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact = models.CharField(max_length=100)

class SubAdminAdditional(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

class UsersAdditional(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    mid_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    full_Add = models.CharField(max_length=200)
    phone = models.CharField(max_length=50)
# End Extra fields

# Model Manager for Proxy Models
class AdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.ADMIN)

class SubAdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type =CustomUser.Types.SUB_ADMIN)

class UserManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type = CustomUser.Types.USER)


# Proxy Model they do not Create a seprate Table
class Admin(CustomUser):
    default_type = CustomUser.Types.ADMIN
    objects = AdminManager()
    class Meta:
        proxy = True
    def all(self):
        print("i can do anythink")
    # Here Create Instance
    @property
    def showAdditional(self):
        return self.adminadditional

class Sub_Admin(CustomUser):
    default_type = CustomUser.Types.SUB_ADMIN
    objects = SubAdminManager()
    class Meta:
        proxy = True
    def add(self):
        print("Only Add")
    # Here Create Instance
    @property
    def showAdditional(self):
        return self.subadminadditional


class User(CustomUser):
    default_type = CustomUser.Types.USER
    objects = UserManager()
    class Meta:
        proxy = True
    def show(self):
        print("Only Show")
    
    # Here Create Instance
    @property
    def showAdditional(self):
        return self.useradditional


class Module(models.Model):
    module_name = models.CharField(max_length=200)