from . import views
from django.urls import path

urlpatterns = [
    path('register', views.register, name='register'),
    path("login", views.login, name='login'),
    path('application_form', views.application_form_view, name='application_form'),
    path('success', views.success, name='success'),
    path('logout', views.logout, name='logout'),


]
