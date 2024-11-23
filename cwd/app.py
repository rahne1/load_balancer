from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f'This is the {os.environ['APP']} application.'

if __name__ == '__main__':
    app.run(host='0.0.0.0')