import json
import pytest

from django.contrib.auth.models import User


def create_user():
    """
    Create a simple user for testing API
    """
    User.objects.create_user(
        username='user',
        email='user@adsf.com',
        password='123'
    )


def auth_client(client):
    """
    Authenticate given client for testing purposes
    """
    create_user()
    client.login(username='user', password='123')
    return client


def test_login_wrong_method(client):
    """
    GET requests should not work at all
    """
    resp = client.delete('/api/login')
    assert resp.status_code == 400
    assert resp['Content-Type'] == 'application/json'
    assert "sessionid" not in resp.cookies

    j = json.loads(resp.content)
    assert j['message'] == "GET or POST method required"


@pytest.mark.django_db
def test_login_wrong_password(client):
    """
    Try to log in with wrong credentials
    """
    create_user()
    resp = client.post('/api/login',
                       content_type='application/json',
                       data=json.dumps({
                           "username": "user",
                           "password": "asdf"
                       }))
    assert resp.status_code == 400
    assert resp['Content-Type'] == 'application/json'
    assert "sessionid" not in resp.cookies

    j = json.loads(resp.content)
    assert j['message'] == "Wrong credentials"


def test_login_malformed_json(client):
    """
    Ensure that malformed requests will not work
    """

    # params instead of JSON
    resp = client.post('/api/login', {
        "username": "user",
        "password": "asdf"
    })

    # wrong headers
    resp = client.post('/api/login',
                       content_type='application/text',
                       data=json.dumps({
                           "username": "user",
                           "password": "asdf"
                       }))
    assert resp.status_code == 400

    # no password
    resp = client.post('/api/login',
                       content_type='application/json',
                       data=json.dumps({
                           "username": "user"
                       }))
    assert resp.status_code == 400

    # no username
    resp = client.post('/api/login',
                       content_type='application/json',
                       data=json.dumps({
                           "password": "asdf"
                       }))
    assert resp.status_code == 400


@pytest.mark.django_db
def test_login_success(client):
    """
    Log in with correct headers and credentials
    """
    create_user()
    resp = client.post('/api/login',
                       content_type='application/json',
                       data=json.dumps({
                           "username": "user",
                           "password": "123"
                       }))
    assert resp.status_code == 200
    assert resp['Content-Type'] == 'application/json'
    assert "sessionid" in resp.cookies

    j = json.loads(resp.content)
    assert sorted(j.keys()) == ['email', 'first_name', 'is_admin', 'last_name', 'username']


def test_login_unauth_get(client):
    """
    unauth GET requests should return an error
    """
    resp = client.get('/api/login')
    assert resp.status_code == 403
    assert resp['Content-Type'] == 'application/json'
    assert "sessionid" not in resp.cookies

    j = json.loads(resp.content)
    assert j['message'] == "not authenticated"


@pytest.mark.django_db
def test_login_auth_get(client):
    """
    auth GET requests should return current user model
    """
    auth_client(client)

    resp = client.get('/api/login')
    assert resp.status_code == 200
    assert resp['Content-Type'] == 'application/json'

    j = json.loads(resp.content)
    assert sorted(j.keys()) == ['email', 'first_name', 'is_admin', 'last_name', 'username']


@pytest.mark.django_db
def test_login_logout(client):
    """
    Log in and then logout
    """
    # FIXME: not implemented
    pass