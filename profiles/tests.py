import pytest

@pytest.mark.django_db
def test_profiles_endpoint(client):
    response = client.get('/api/profiles/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_profile(client):
    data = {
        "name": "Test User",
        "bio": "Testing bio"
    }
    response = client.post('/api/profiles/', data)

    assert response.status_code == 201