import pytest


class TestUserAPI:

    @pytest.mark.django_db(transaction=True)
    def test_users_authenticated(self, user_client):
        response = user_client.get('/api/auth/users/me/')

        assert response.status_code != 404, (
            'Page `/api/auth/users/me/` not found, check' +
            'this adress in *urls.py*'
        )

        assert response.status_code == 200, (
            'Check that on GET request `/api/auth/users/`' +
            'return status 200'
        )
