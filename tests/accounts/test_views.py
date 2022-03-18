import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestAccounts:

    def test_render_get(self, client):
        url = reverse('accounts')
        response = client.get(url)
        assert response.status_code == 200
        assert response.charset == 'utf-8'

        html = response.content.decode()
        assert 'Login' in html
        assert response.headers
        assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'
