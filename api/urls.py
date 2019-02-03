from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('feed/detail/', views.FeedDetailView.as_view(), name='feed-detail'),
]
