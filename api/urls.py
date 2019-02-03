from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from api import views

app_name = 'api'

urlpatterns = [
    path('feed/detail/', views.FeedDetailView.as_view(), name='feed-detail'),
    path('feed/detail/no-auth/', views.FeedDetailAllowAnyView.as_view(), name='feed-detail-no-auth'),
    path('token/', obtain_auth_token, name='obtain-auth-token')
]
