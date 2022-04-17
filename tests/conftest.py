import pytest


@pytest.fixture
def user(django_user_model):
    return django_user_model.objects.create_user(
        username='TestUser', email='testuser@mail.fake', password='12345qwerty',
        first_name='test', last_name='testset'
    )


@pytest.fixture
def token_user(user):
    from rest_framework_simplejwt.tokens import AccessToken
    token = AccessToken.for_user(user)

    return {
        'access': str(token),
    }


@pytest.fixture
def user_client(token_user):
    from rest_framework.test import APIClient

    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token_user["access"]}')
    return client