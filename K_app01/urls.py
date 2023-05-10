from django.urls import path
from . import views
from .views import CustomLoginView


urlpatterns = [
    path('', views.home, name='home'),
    path('add-expense/', views.add_expense, name='add_expense'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/login/', CustomLoginView.as_view(), name='register'),

]