from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return product

product = [
    {"productId": "10",
     "transactionAmount": "1000.0",
     "transactionDatetime": "2018-10-01 10:10:10"}
]


