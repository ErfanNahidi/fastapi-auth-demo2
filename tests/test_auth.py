import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register_and_login():
    # register
    res = client.post('/auth/register', json={"email":"a@b.com","password":"secret"})
    assert res.status_code == 200
    data = res.json()
    assert data['email'] == 'a@b.com'

    # login
    res2 = client.post('/auth/token', data={"username":"a@b.com","password":"secret"})
    assert res2.status_code == 200
    assert 'access_token' in res2.json()