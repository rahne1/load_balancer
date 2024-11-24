import pytest 

from cwd.load_balancer import load_balancer

@pytest.fixture
def client():
    with load_balancer.test_client() as client:
        yield client
        
def test_host_routing_mango(client):
    result = client.get('/', headers={'Host': 'www.mango.com'})
    assert b'This is the mango application.' in result.data
    

def test_host_routing_apple(client):
    result = client.get('/', headers={'Host': 'www.apple.com'})
    print(result)
    assert b'This is the apple application.' in result.data
    
def test_host_routing_notfound(client):
    result = client.get('/', headers={'Host': 'www.notmango.com'})
    assert b'Not Found' in result.data
    assert 404 == result.status_code
    
def test_path_routing_mango(client):
    result = client.get('/mango')
    assert b'This is the mango application.' in result.data
def test_path_routing_apple(client):
    result = client.get('/apple')
    assert b'This is the apple application.' in result.data 
def test_path_routing_notfound(client):
    result = client.get('/notmango')
    assert b'Not Found' in result.data
    assert 404 == result.status_code