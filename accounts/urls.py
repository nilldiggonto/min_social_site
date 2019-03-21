from django.urls import path
from .views import UserDetailView
app_name='account'
urlpatterns = [
    path('<str:user>/',UserDetailView.as_view(),name='user_detail'),
]
