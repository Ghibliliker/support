import pytest


class TestUserAPI:

    @pytest.mark.django_db(transaction=True)
    def test_01_users_not_authenticated(self, client):
        response = client.get('/api/auth/users/')

        assert response.status_code != 404, (
            'Страница `/api/auth/users/` не найдена, проверьте этот адрес в *urls.py*'
        )

        assert response.status_code == 200, (
            f'Проверьте, что при GET запросе `/api/auth/users/` возвращается статус 200'
        )