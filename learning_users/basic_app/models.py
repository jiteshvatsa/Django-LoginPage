from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    # additional attributes
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username
