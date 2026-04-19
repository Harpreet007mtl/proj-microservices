import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/user')
def getusers():
    name = request.args.get('name')
    if name:
        # Call cart service to add user to cart
        response = requests.get(f'http://cart:5001/cart?name={name}')
        return f'Hello {name}. {response.text}'
    else:
        return 'Hello, World!'  # Default if no name provided

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Different port to avoid conflict
