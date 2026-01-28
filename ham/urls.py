# from django.contrib import admin
from django.urls import path

from . import views 
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
   
    path('',views.ham_list, name='ham_list'),
    path('create/', views.ham_create, name='ham_create'),
    path('<int:user_id>/edit/', views.ham_edit, name='ham_edit'),
    path('<int:user_id>/delete/', views.ham_delete, name='ham_delete'),
    path('register/', views.register, name='register'),
]