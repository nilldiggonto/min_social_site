from django.urls import path
from .views import Imi_list_view,Imi_detail_view,Imi_create_view ,Imi_update_view,Imi_delete_view
from imi_social.views import home
app_name ='post'

urlpatterns = [
    path('',home,name='home'),
    path('list/',Imi_list_view.as_view(),name='list'),
    path('create/',Imi_create_view.as_view(),name='create'),
    path('detail/<int:pk>',Imi_detail_view.as_view(),name='detail'),
    path('update/<int:pk>',Imi_update_view.as_view(),name='update'),
    path('delete/<int:pk>',Imi_delete_view.as_view(),name='delete'),
    
]
