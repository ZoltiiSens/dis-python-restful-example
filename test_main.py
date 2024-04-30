from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_root():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {'hello': 'world!'}


def test_root_1():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() != {'hello': 'world!!!'}