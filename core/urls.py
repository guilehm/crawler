from django.urls import path

from core import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('feed/detail/', views.signup, name='feed-detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
]
