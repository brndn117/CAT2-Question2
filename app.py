from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage to hold product data
product_store = []

@app.route('/products', methods=['POST'])
def add_product():
    """Endpoint to create a new product."""
    product_data = request.get_json()

    # Input validation
    required_fields = ['name', 'description', 'price']
    if not product_data or not all(field in product_data for field in required_fields):
        return jsonify({'error': 'Missing or invalid input fields'}), 400

    # Create and save the new product
    new_product = {
        'name': product_data['name'],
        'description': product_data['description'],
        'price': product_data['price']
    }
    product_store.append(new_product)
    return jsonify(new_product), 201

@app.route('/products', methods=['GET'])
def list_products():
    """Endpoint to retrieve all products."""
    return jsonify(product_store), 200

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
