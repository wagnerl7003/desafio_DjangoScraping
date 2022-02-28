from . import views
from django.urls import path

urlpatterns = [
    path('delete/<int:proxy_pk>', views.DeleteProxy, name='deleteproxy' ),
    path('edit/<int:proxy_pk>', views.EditProxy, name='editproxy' ),
    path('add/', views.InsertProxy, name='addproxy' ),
    path('', views.home, name='home'),


]