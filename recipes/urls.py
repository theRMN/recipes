from django.urls import path
from calculator import views

urlpatterns = [
    path('<dish>/', views.recipes)
]
