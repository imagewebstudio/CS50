from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


def user_directory_path(instance, filename):
     #file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class User(AbstractUser):
    USER_TYPE_CHOICES = [
      (3, 'cashier'),
      (6, 'supervisor'),
      (9, 'Account Manager'),
    ]
    USER_LEVEL_CHOICES = [
      (3, 'free'),
      (6, 'silver'),
      (9, 'gold'),
    ]
    position = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)
    company = models.CharField(max_length=99)
    level = models.PositiveSmallIntegerField(choices=USER_LEVEL_CHOICES, null=True, blank=True)
    account_manager = models.CharField(max_length=300, null=True)
    dob = models.DateField(null=True)
    pin = models.PositiveSmallIntegerField(null=True)
    pass

class Store(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="stores")
    cashiers = models.ManyToManyField(User, blank= True, related_name="store")
    pass

class Inventory(models.Model):
    STATUS_CHOICES = [
      (9, 'active'),
      (3, 'inactive'),
    ]
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    barcode = models.CharField(max_length=100)
    title = models.TextField(max_length=100)
    image = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    discription = models.CharField(max_length=1000)
    stock = models.PositiveSmallIntegerField(null=True, blank=True)
    tax = models.PositiveSmallIntegerField(null=True, blank=True)
    store = models.ForeignKey(Store,null=True, blank=True, on_delete=models.CASCADE, related_name="items")
    price = models.PositiveSmallIntegerField(null=True, blank=True)
    cost = models.PositiveSmallIntegerField(null=True, blank=True)
    pass

class Register(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="registers")
    cash = models.DecimalField(max_digits=8, decimal_places=2)
    pass

class Reciept(models.Model):
    text = models.CharField(max_length=10000, null=True, blank=True )
    pass

class Transactions(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="transactions", null=True)
    time = models.DateTimeField(auto_now_add=True)
    cashier = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    register = models.PositiveSmallIntegerField(null=True)
    items = models.ManyToManyField(Inventory, related_name="transactions", blank=True)
    reciept = models.ManyToManyField(Reciept, related_name="transaction", blank=True)
    status = models.CharField(max_length=15)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    def serialize(self):
        return { "id": self.id, "store": self.store.name, "time": self.time, "cashier": self.cashier.username, "reciept": self.reciept, "total": self.total
        }


class Movement(models.Model):
    STATUS_CHOICES = [
      (9, 'in'),
      (3, 'out'),
    ]
    store = models.ForeignKey(Store, on_delete=models.CASCADE, related_name="cashlog", blank = True )
    cashier = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cashlog")
    register = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="cashlog", blank = True )
    total = models.PositiveSmallIntegerField()
    time = models.DateTimeField(auto_now_add=True)
    transaction = models.CharField(max_length=30)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)
    qty = models.PositiveSmallIntegerField()
    pass

class Cashierlog(models.Model):
    LOG_CHOICES = [
      (9, 'login'),
      (3, 'logged out'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="log")
    register = models.ForeignKey(Register, on_delete=models.CASCADE, related_name="cashierlog")
    time = models.DateTimeField(auto_now_add=True)
    logged = models.PositiveSmallIntegerField(choices=LOG_CHOICES)
    pass
