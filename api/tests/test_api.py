import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestApi:

    @pytest.fixture
    def public_client(self):
        public_client = APIClient()
        return public_client

    @pytest.fixture
    def user(self):
        user = User.objects.create(
            username='usuario',
            password='senhasegura',
            is_active=True,
        )
        Token.objects.create(user=user)
        return user

    def test_feed_detail_no_auth_response_status(self, client):
        url = reverse('api:feed-detail-no-auth')
        response = client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_feed_detail_should_authorize_requests_with_token(self, client, user):
        url = reverse('api:feed-detail')
        response = client.get(url, HTTP_AUTHORIZATION=f'Token {user.auth_token}')
        assert response.status_code == status.HTTP_200_OK

    def test_feed_detail_should_not_authorize_requests_without_token(self, client):
        url = reverse('api:feed-detail')
        response = client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
