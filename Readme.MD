### Testing the API

List All Categories
GET /categories/
Response:

json
Copy code
[
    {
        "id": 1,
        "name": "Electronics",
        "description": "Devices and gadgets.",
        "created_at": "2025-01-01T12:00:00Z",
        "updated_at": "2025-01-01T12:00:00Z"
    }
]
Create a Category
POST /categories/
Request Body:

json
Copy code
{
    "name": "Clothing",
    "description": "Apparel and garments."
}
List All Products
GET /products/
Response:

json
Copy code
[
    {
        "id": 1,
        "name": "Laptop",
        "description": "A high-performance laptop.",
        "price": "1200.00",
        "stock": 50,
        "category": {
            "id": 1,
            "name": "Electronics",
            "description": "Devices and gadgets.",
            "created_at": "2025-01-01T12:00:00Z",
            "updated_at": "2025-01-01T12:00:00Z"
        },
        "created_at": "2025-01-01T12:00:00Z",
        "updated_at": "2025-01-01T12:00:00Z"
    }
]
Create a Product
POST /products/
Request Body:

json
Copy code
{
    "name": "Smartphone",
    "description": "A cutting-edge smartphone.",
    "price": "800.00",
    "stock": 100,
    "category_id": 1
}


### Test the Authentication System

Testing Steps:
Login Endpoint (POST /auth/login/):

Send a POST request with username and password in the body.
Example Request:
json
Copy code
{
    "username": "testuser",
    "password": "testpassword"
}
Response:
json
Copy code
{
    "token": "c8f7a0f6a91b12e34e5d77e0b3d66d6b88574e45"
}
Access Protected Endpoints:

Include the token in the Authorization header of the request:
makefile
Copy code
Authorization: Token <token>
Example cURL Command:
bash
Copy code
curl -H "Authorization: Token c8f7a0f6a91b12e34e5d77e0b3d66d6b88574e45" http://127.0.0.1:8000/products/
Logout Endpoint (POST /auth/logout/):

Send a POST request (no body required) with the token in the header.
Example Response:
json
Copy code
{
    "message": "Logged out successfully."
}
Step 8: Add Documentation
Create a README.md file in your repository to explain the authentication setup.

Example README.md
markdown
Copy code

# Authentication Setup

## Login Endpoint

**URL:** `/auth/login/`  
**Method:** `POST`  
**Body:**  
```json
{
    "username": "your_username",
    "password": "your_password"
}
Response:

json
Copy code
{
    "token": "your_generated_token"
}
Logout Endpoint
URL: /auth/logout/
Method: POST
Header:

makefile
Copy code
Authorization: Token <your_token>
Response:

json
Copy code
{
    "message": "Logged out successfully."
}
Using the Token
Include the token in the Authorization header for all protected endpoints:

makefile
Copy code
Authorization: Token <your_token>
yaml
Copy code

---

### **Step 9: Push to GitHub**
1. Commit the changes to your repository.
2. Push the updated code to GitHub.
3. Include all relevant files, including `README.md`, in your repository.
