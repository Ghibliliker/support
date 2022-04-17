import pytest

from .common import create_ticket


class TestTicketAPI:

    @pytest.mark.django_db(transaction=True)
    def test_ticket_not_auth(self, user_client):
        response = user_client.get('/api/v1/tickets/')
        assert response.status_code != 404, (
            'Страница `/api/v1/tickets/` не найдена, проверьте этот адрес в *urls.py*'
        )
        assert response.status_code == 200, (
            'Проверьте, что при GET запросе `/api/v1/tickets/` без токена авторизации возвращается статус 200'
        )

    @pytest.mark.django_db(transaction=True)
    def test_ticket_auth(self, user_client):
        data = {'name': 'name', 'text': 'text'}
        response = user_client.post('/api/v1/tickets/', data=data)
        assert response.status_code == 201, (
            'Проверьте, что при POST запросе `/api/v1/tickets/` с правильными данными возвращает статус 201'
        )
