import pytest


class TestTicketAPI:

    @pytest.mark.django_db(transaction=True)
    def test_ticket_url_auth(self, user_client):
        response = user_client.get('/api/v1/tickets/')
        assert response.status_code != 404, (
            'Page `/api/v1/tickets/` not found, check' +
            'this adress in *urls.py*'
        )
        assert response.status_code != 403, (
            'Check that on GET request `/api/v1/tickets/`' +
            'without authorization token returns status 403'
        )

    @pytest.mark.django_db(transaction=True)
    def test_ticket_post_auth(self, user_client):
        data = {'name': 'name', 'text': 'text'}
        response = user_client.post('/api/v1/tickets/', data=data)
        assert response.status_code == 201, (
            'Check that on POST request `/api/v1/tickets/`' +
            'with valid data returns status 201'
        )
