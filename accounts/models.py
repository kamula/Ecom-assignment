from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
import uuid


class AccountManager(BaseUserManager):
    def create_user(self,firstName,lastName,email,phoneNumber,password = None):
        if not firstName:
            return ValueError('first name required')
        if not lastName:
            return ValueError('last name required')
        if not phoneNumber:
            return ValueError('phone number required')
        if not email:
            return ValueError('email required')
        user = self.model(
            firstName = firstName,
            lastName = lastName,
            phoneNumber = phoneNumber,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,firstName,lastName,email,phoneNumber,password):
        user = self.create_user(
            firstName=firstName,
            lastName=lastName,
            email=self.normalize_email(email),
            phoneNumber=phoneNumber,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50,unique=True,default=uuid.uuid1)
    email = models.EmailField(max_length=100,unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName','lastName','phoneNumber']
    objects = AccountManager()

    def __str__(self):
        return self.email

    
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True

