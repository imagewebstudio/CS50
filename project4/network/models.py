from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.CharField(max_length=300, default="images/userpic.png")
    following = models.ManyToManyField('self', blank=True, related_name="followed_by")
    followed_by = models.ManyToManyField('self', blank=True, related_name="following")
    dob = models.DateTimeField(auto_now_add=False)
    pass

class Post(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=1800)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    liked_by = models.ManyToManyField(User, blank=True, related_name="liked")
    unliked_by = models.ManyToManyField(User, blank=True, related_name="unliked")
    def __str__(self):
        return f"{self.time} {self.text} {self.user} {self.liked_by} {self.unliked_by}"

class Comment(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=600)
    usersname = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    listing = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    def __str__(self):
        return f"{self.time} {self.text} {self.listing} {self.user}"
