from flask import Flask, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get MongoDB credentials from environment variables
mongodb_username = os.getenv('MONGODB_USERNAME')
mongodb_password = os.getenv('MONGODB_PASSWORD')


# MongoDB connection
mongodb_client = MongoClient(
    f"mongodb+srv://{mongodb_username}:{mongodb_password}@cluster0.9jy65.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = mongodb_client["shop_db"]
products_collection = db["products"]

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/insert-products")
def insert_products():
    mock_data = [
        {"name": "iPhone", "tag": "new", "price": 1459.99, "image_path": "/static/images/iphone.jpg"},
        {"name": "Laptop", "tag": "new", "price": 2459.99, "image_path": "/static/images/laptop.jpg"},
        {"name": "Nokia 5", "tag": "new", "price": 459.99, "image_path": "/static/images/Nokia.jpg"}
    ]
    products_collection.insert_many(mock_data)
    return "Products inserted successfully!"

@app.route("/products")
def products():
    products = products_collection.find()
    return render_template("products.html", products=products)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
