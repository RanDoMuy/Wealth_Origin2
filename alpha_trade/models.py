from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator



class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length= 50)
    number = models.CharField(max_length=20)
    passwd= models.CharField(max_length= 50, blank=True)
    trade_status= models.CharField(("Trade status"), max_length=50, default="Inactive")
    trading_plan= models.CharField(("Trading plan"), max_length=50, default="No plan")
    deposit_balance= models.IntegerField(("Deposit_Balance"), default=50, validators=[MaxValueValidator(9999999999)])
    profit_balance= models.IntegerField(("Profit Balance"), default=0, validators=[MaxValueValidator(9999999999)])
    country= models.CharField(("Country"), default="none", max_length= 50)
    verify= models.BooleanField(default= False)
    image = models.ImageField(upload_to='images/', blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

class Deposit_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount= models.IntegerField(("Deposit Balance"), blank= True, validators=[MaxValueValidator(9999999999)])
    timestamp= models.DateTimeField(("Date"), auto_now_add=True)
    status= models.CharField(("Deposit Status"), default= "Pending", max_length= 50)
    method= models.CharField(("Deposit Method"), default= "Bitcoin", max_length= 50)

    def __str__(self):
        return self.user.email
    
class Withdrawal_History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount= models.IntegerField(("Deposit Balance"), blank= True, validators=[MaxValueValidator(9999999999)])
    timestamp= models.DateTimeField(("Date"), auto_now_add=True)
    status= models.CharField(("Deposit Status"), default= "Pending", max_length= 50)
    method= models.CharField(("Deposit Method"), default= "Bitcoin", max_length= 50)

    def __str__(self):
        return self.user.email
    

class Investment_Plan(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name