from django.urls import path
from . import views

app_name = 'user'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('doregister/', views.doregister, name='doregister'),
    path('dologin/', views.dologin, name='dologin'),
    path('logout/', views.logout, name='logout'),
    path('isRegistered/', views.isRegistered, name='isRegistered'),
]