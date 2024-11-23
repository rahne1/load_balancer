import pytest 

from load_balancer import load_balancer

@pytest.fixture
def client():
    with load_balancer.test_client() as client:
        yield client
        
def test_hello(client):
    result = client.get('/')
    assert b'hello' in result.data
