import requests
import json

BASE_URL = 'http://127.0.0.1:5000'  # Replace with actual server URL if different

def create_product(name, description, price):
    url = f'{BASE_URL}/products'
    data = {'name': name, 'description': description, 'price': price}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print('Product 1  created successfully!')
        print(response.json())
    else:
        print(f'Error creating product: {response.status_code}')
        print(response.text)

def get_products():
    url = f'{BASE_URL}/products'
    response = requests.get(url)

    if response.status_code == 200:
        products = response.json()
        print('Products:')
        for product in products:
            print(f"- Name: {product['name']}")
            print(f"  Description: {product['description']}")
            print(f"  Price: ${product['price']:.2f}")  # Format price with 2 decimals
            print()  # Add a new line after each product

if __name__ == '__main__':
    while True:
        print("\nMenu:")
        print("1. Create Product")
        print("2. Get Products")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            create_product(name, description, price)
        elif choice == '2':
            get_products()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")