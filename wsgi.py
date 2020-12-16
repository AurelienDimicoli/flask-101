from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world A!"


PRODUCTS = {
    1: {'id': 1, 'name': 'Skello'},
    2: {'id': 2, 'name': 'Socialive.tv'},
    3: {'id': 3, 'name': 'LeWagonPA'}
}


@app.route('/api/v1/products')
def products():
    return jsonify(PRODUCTS)
