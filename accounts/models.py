from django.db import models
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL,related_name ='profile',on_delete='DO_NOTHING' )
    follow      = models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name ='followed_by')


    def __str__(self):
        return str(self.follow.all().count())
    
