from django.urls import path

from . import views

urlpatterns = [
    path('getPortfolios/', views.get_list_portfolios, name='getPortfolios'),
]