from django.db import models
from django.urls import reverse
from django.conf import settings
from imi_social.validators import validate_content
User = settings.AUTH_USER_MODEL
# Create your models here.


class ImiStatus(models.Model):
    user        = models.ForeignKey(User,on_delete='DO_NOTHING')
    content     = models.CharField(max_length=150,validators=[validate_content,])
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp',]



    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"pk": self.pk})
    def get_update_url(self):
        return reverse('post:update',kwargs={'pk':self.pk})

    def get_delete_url(self):
        return reverse('post:delete',kwargs={'pk':self.pk})

    def get_user_url(self):
        return reverse('account:user_detail',kwargs={'user':self.user})
    # def clean(self,*args,**kwargs):
    #     content = self.content
    #     if content == 'abc':
    #         raise ValidationError('Cannot be abc')
    #     return super(ImiStatus,self).clean(*args,**kwargs)
    
    

