from django.contrib.auth.models import AbstractUser
from django.db import models


# Uncomment to add user image via file upload
#def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
#    return 'user_{0}/{1}'.format(instance.user.id, filename)

#class MyModel(models.Model):
    #upload = models.FileField(upload_to=user_directory_path)
    #image = models.FileField(upload_to='uploads/')

class User(AbstractUser):
    since = models.DateTimeField(auto_now_add=True)
    pass

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"

class Listing(models.Model):
    active = models.CharField(max_length=3, default="yes")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    image = models.CharField(max_length=300)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    category = models.ManyToManyField(Category, related_name="listings")
    startprice =  models.DecimalField(max_digits=12, null=True, decimal_places=2)
    currentprice =  models.DecimalField(max_digits=12, null=True, decimal_places=2)
    starts = models.DateTimeField(auto_now_add=True)
    ends = models.DateTimeField(auto_now_add=False, null=True)
    winningbidder = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="bidswon")
    wishlist = models.ManyToManyField(User, blank=True, related_name="wishlist")
    def __str__(self):
        return f"{self.image} {self.title} {self.description} {self.category} {self.startprice} {self.starts} {self.ends}"

class Bid(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, null=True, related_name="bids")
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="bids")
    def __str__(self):
        return f"{self.date} {self.price} {self.listing}"

class Comment(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments")
    def __str__(self):
        return f"{self.time} {self.text}"
