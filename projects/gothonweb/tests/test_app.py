from app import app
from gothonweb import planisphere
import pytest

@pytest.fixture
def web():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(web):
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code == 200

    rv = web.get('/game', follow_redirects=True)
    assert rv.status_code == 200
    
    with web.session_transaction() as sess:
        sess['room_name'] = planisphere.START

    rv = web.post('/game', data={'action': 'tell a joke'}, follow_redirects=True)
    assert rv.status_code == 200
    assert b"Laser" in rv.data