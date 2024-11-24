from flask import Flask, request
import random
import yaml
import requests

load_balancer = Flask(__name__)
mangos = ['localhost:8081', 'localhost:8082']
apples = ['localhost:9081', 'localhost:9082']

def load_config(path):
    with open(path) as cfg_file:
        cfg = yaml.load(cfg_file, Loader=yaml.FullLoader)
    return cfg

cfg = load_config('load_balancer.yml')
@load_balancer.route('/')
def router():
    host_header = request.headers['Host']
    for host in cfg['hosts']:
        if host_header == host['host']:
            response = requests.get(f'http://{random.choice(host['servers'])}')
            return response.content, response.status_code
    return 'Not Found', 404
    
@load_balancer.route('/<path>')
def routing(path):
    for entry in cfg['paths']:
        if f'/{path}' == entry["path"]:
            response = requests.get(f'http://{random.choice(entry["servers"])}')
            return response.content, response.status_code
    return 'Not Found', 404
