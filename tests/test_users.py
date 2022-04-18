import pytest


class TestUserAPI:

    @pytest.mark.django_db(transaction=True)
    def test_users_authenticated(self, user_client):
        response = user_client.get('/api/auth/users/')

        assert response.status_code != 404, (
            'Страница `/api/auth/users/` не найдена, проверьте' +
            'этот адрес в *urls.py*'
        )

        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/auth/users/`' +
            'возвращается статус 200'
        )
