from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address!")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    


    def create_super(self, email, username, password):
        user = self.create_super(
            email=self.normalize_email(email),
            password=password,
            uername=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



class Account(models.Model):
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    mobile = PhoneNumberField(unique=True, region="IR")
    date_joined = models.DateTimeField(auto_now_add=True)
    hide_email = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username', 'mobile']
    objects = MyAccountManager()

    def __str__(self):
        return f"{self.email}"
