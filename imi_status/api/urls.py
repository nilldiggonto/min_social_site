from django.urls import path
from .views import ImiListApiView,ImiCreateApiView
app_name = 'api'
urlpatterns = [
    path('',ImiListApiView.as_view(),name='listapi'),
    path('create/',ImiCreateApiView.as_view(),name='createapi'),
]
