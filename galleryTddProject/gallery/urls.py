from django.urls import path

from . import views

urlpatterns = [
    path('getPortfolios/', views.get_list_portfolios, name='getPortfolios'),
    path('users/', views.users, name='users'),
    path('users/<int:id>', views.users, name='users'),
    path('users/<int:id>/portafolio', views.portafolio_usuario, name='portafolioUsuario'),
    path('login/', views.login, name='login'),
    path('modifyImageStatus/', views.modify_imageStatus, name='modifyImageStatus'),
    path('addImage/<int:id>/', views.add_image_portfolio, name='addImage')
]