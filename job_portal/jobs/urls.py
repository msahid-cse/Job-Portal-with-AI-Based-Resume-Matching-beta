# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout
]
