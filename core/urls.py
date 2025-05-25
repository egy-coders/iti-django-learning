from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    
]