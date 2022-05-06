import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_accounts(client):
    url = reverse('accounts')
    response = client.get(url)
    assert response.status_code == 200
    assert response.charset == 'utf-8'

    html = response.content.decode()
    assert 'Login' in html
    assert response.headers
    assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

@pytest.mark.django_db
def test_register(client):
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200
    assert response.charset == 'utf-8'

    html = response.content.decode()
    assert 'Cadastro' in html
    assert response.headers
    assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'

@pytest.mark.django_db
def test_complement_register(client):
    url = reverse('complement_register')
    response = client.get(url)
    assert response.status_code == 200
    assert response.charset == 'utf-8'

    html = response.content.decode()
    assert 'Complemento' in html
    assert response.headers
    assert response.headers.get('Content-Type') == 'text/html; charset=utf-8'
