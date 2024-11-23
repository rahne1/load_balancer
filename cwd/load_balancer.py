from flask import Flask, request
import random
import requests

load_balancer = Flask(__name__)
mangos = ['localhost:8081, localhost:8082']
apples = ['localhost:9081, localhost:9082']

@load_balancer.route('/')
def router():
    host_header = request.headers['Host']
    if host_header == 'www.mango.com':
        response = requests.get(f'http://{random.choice(mangos)}')
        return response.content, response.status_code
    elif host_header == 'www.apple.com':
        response = requests.get(f'http://{random.choice(apples)}')
        return response.content, response.status_code
    else:
        return 'Not Found', 404
    
        