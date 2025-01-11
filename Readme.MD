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
