Installation:

Clone the Repository:
git clone https://github.com/[your_username]/rest_api_products.git

Create a Virtual Environment:
cd rest_api_products
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows


Install Dependencies:
Bash
pip install Flask flask_restful requests


Running the API
Start the Flask App:
python app.py


The API will be accessible at http://127.0.0.1:5000 by default.
API Endpoints
POST /products
Request Body: JSON object with name, description, and price fields.
Response:
201 Created: On successful product creation
400 Bad Request: If input data is invalid or missing
GET /products
Response:
200 OK: Returns a JSON array of all products
Client Interaction
Run the Client Script:
Bash
python client.py
Use code with caution.

Follow the Prompts:
Add new products
Retrieve and view the product list