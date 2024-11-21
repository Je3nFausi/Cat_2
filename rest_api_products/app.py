from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

class Products(Resource):
    def post(self):
        data = request.get_json()

        if not data or not all(key in data for key in ['name', 'description', 'price']):
            return jsonify({'error': 'Missing required fields'}), 400

        # Validate data types
        if not isinstance(data['name'], str):
            return jsonify({'error': 'Invalid name format (must be a string)'}), 400
        if not isinstance(data['description'], str):
            return jsonify({'error': 'Invalid description format (must be a string)'}), 400
        try:
            price = float(data['price'])
            if price <= 0:
                return jsonify({'error': 'Price must be positive'}), 400
        except ValueError:
            return jsonify({'error': 'Invalid price format (must be a number)'}), 400

        try:
            # Simulate product creation logic (in-memory storage for simplicity)
            products.append(data)
            return jsonify(data), 201  # Created

        except Exception as e:
            return jsonify({'error': str(e)}), 500  # Internal Server Error

    def get(self):
        return jsonify(products), 200  # OK

# Mock product data (replace with database or persistence layer)
products = []

api.add_resource(Products, '/products')

if __name__ == '__main__':
    app.run(debug=True)