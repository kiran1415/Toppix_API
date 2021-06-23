from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings 
from . import views
urlpatterns = [
    path('toppix',views.toppix,name='toppix'),
    path('toppix/<int:pk>',views.get_toppix,name='get_toppix'),
    path('delete_toppix/<int:pk>',views.delete_toppix,name='delete_toppix'),
    path('create_like_toppix/<int:pk>',views.create_like_toppix,name='create_like_toppix'),
    path('create_view_toppix/<int:pk>',views.create_view_toppix,name='create_view_toppix'),
    path('create_share_toppix/<int:pk>',views.create_share_toppix,name='create_share_toppix'),
    path('create_download_toppix/<int:pk>',views.create_download_toppix,name='create_download_toppix'),
    
]
