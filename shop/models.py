from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)


    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now = True)
    phone = models.CharField(max_length=25, blank = True)
    adress1 = models.CharField(max_length=250, blank = True)
    adress2 = models.CharField(max_length=250, blank = True)
    city = models.CharField(max_length=25, blank = True)
    state = models.CharField(max_length=25, blank = True)
    zipcode = models.CharField(max_length=25, blank = True)
    country = models.CharField(max_length=25, default = 'IRAN')
    old_cart = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
post_save.connect(create_profile, sender=User)
    
class Product(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=500, default= '', blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=0, max_digits=12)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    picture = models.ImageField(upload_to='upload/product/')
    star = models.IntegerField(default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=0, max_digits=12)

    def __str__(self):
        return self.name
    

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=400, default='', blank=True)
    phone = models.CharField(max_length=15, blank=False)
    date = models.DateField(default=datetime.datetime.today())
    status = models.BooleanField(default=False)


    def __str__(self):
        return self.product
    

