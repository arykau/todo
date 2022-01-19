from django.urls import path
from . import views
from .views import LoginPage, RegisterPage
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("login/", LoginPage.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page='login'), name="logout"),
    path("register/", RegisterPage.as_view(), name="register"),

    path('', views.home_page, name="tasks"),
    path('task/<int:pk>/', views.task_detail, name="description"),

    path('add/', views.task_add, name="add"),
    path('update/<int:pk>/', views.task_update, name="update"),
    path('delete/<int:pk>/', views.task_delete, name="delete"),
]
