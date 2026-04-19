import requests
from flask import Flask, request

app = Flask(__name__)

cart = []  # Simple in-memory cart list

@app.route('/cart')
def add_to_cart():
    name = request.args.get('name')
    if name:
        cart.append(name)
        return f'Added {name} to cart. Cart contents: {cart}'
    else:
        return 'Please provide a name parameter, e.g., /cart?name=John'

@app.route('/cart/view')
def view_cart():
    return f'Cart contents: {cart}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Different port to avoid conflict