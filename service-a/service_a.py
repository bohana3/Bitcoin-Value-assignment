from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

def generate_random_bitcoin_value():
    timestamp = datetime.now().isoformat()

    bitcoin_value = round(random.uniform(5000, 60000), 2)

    return timestamp, bitcoin_value

@app.route('/bitcoin_value')
def get_bitcoin_value():
    timestamp, bitcoin_value = generate_random_bitcoin_value()
    response = {
        "message": f"Service A, bitcoin value is {bitcoin_value}$ for '{timestamp}'",
        "timestamp": timestamp,
        "bitcoin_value": bitcoin_value
    }
    return jsonify(response)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000)
