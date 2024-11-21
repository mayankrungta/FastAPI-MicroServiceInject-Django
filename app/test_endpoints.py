from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_home():
    response = client.get('/')
    assert response.status_code == 200
    assert "text/html" in response.headers['content-type']
    assert "<h1>Howdie John!</h1>" in response.text


def test_post_home():
    response = client.post("/")
    assert response.status_code == 200
    assert "application/json" in response.headers['content-type']
    assert response.json() == {"msg": "FooBar"}
