from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profiles', blank=True, null=True)

    def __str__(self):
        return self.user.username

