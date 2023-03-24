from flask import Flask
from flask import request
from btcpay import BTCPayClient
import numpy as np

#client = BTCPayClient.create_client(host='http://localhost', code="kGNPyHb")

app = Flask(__name__)

database = []

try:
    database = np.load("database.npy", allow_pickle=True)
except Exception as e:
    np.save("database", database)

@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/newTransactionBeingMade', methods=["GET", "POST"])
def about():
    return '<h3>This is a Flask web application.</h3>'

@app.route('/paymentSettled', methods=["GET", "POST"])
def about2():
    global database
    database = np.append(database, request.json)
    np.save("database", database)
    return 'Saved'


app.run(host="172.17.0.1")