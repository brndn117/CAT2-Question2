import requests

# Base URL for the API
API_BASE_URL = "http://127.0.0.1:5000/products"

def create_product(product_name, product_description, product_price):
    """
    Sends a POST request to add a new product to the API.

    Args:
        product_name (str): Name of the product.
        product_description (str): Description of the product.
        product_price (float): Price of the product.
    """
    product_payload = {
        "name": product_name,
        "description": product_description,
        "price": product_price
    }
    response = requests.post(API_BASE_URL, json=product_payload)
    if response.status_code == 201:
        print("✅ Product successfully added!")
    else:
        print(f"❌ Error adding product: {response.json()}")

def fetch_products():
    """
    Sends a GET request to retrieve the list of all products.
    """
    response = requests.get(API_BASE_URL)
    if response.status_code == 200:
        product_list = response.json()
        print("📋 Available Products:")
        for idx, product in enumerate(product_list, start=1):
            print(f"{idx}. {product}")
    else:
        print("❌ Error fetching products.")

if __name__ == "__main__":
    # Demonstration of the client functionality
    create_product("Gaming Laptop", "Powerful gaming laptop with RTX graphics", 1500.00)
    create_product("Smartphone", "5G enabled smartphone with OLED display", 899.99)
    fetch_products()
