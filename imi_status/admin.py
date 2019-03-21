from django.contrib import admin
from .forms import ImiModelForm
from .models import ImiStatus

# Register your models here.
# admin.site.register(ImiStatus)

class ImiModelAdmin(admin.ModelAdmin):
    
    class Meta:
        model = ImiStatus
        
admin.site.register(ImiStatus,ImiModelAdmin)
