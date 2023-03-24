from flask import Flask
from flask import request
from btcpay import BTCPayClient
import numpy as np

#client = BTCPayClient.create_client(host='http://localhost', code="kGNPyHb")

app = Flask(__name__)

try:
    database = np.load("database.npy")
except Exception as e:
    database = []
    np.save("database", database)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/newTransactionBeingMade', methods=["GET", "POST"])
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/paymentSettled', methods=["GET", "POST"])
def about2():
    return '<h3>This is a Flask web application.</h3>'


app.run(host="0.0.0.0")