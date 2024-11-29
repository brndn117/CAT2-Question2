# REST API for Product Management

## Overview
This is a simple REST API built using Flask for managing products. Each product has the following fields:
- `name` (string): Product name
- `description` (string): Product description
- `price` (float): Product price

---

## Endpoints

### 1. POST `/products`
- **Description**: Creates a new product.
- **Request Body**:
  ```json
  {
    "name": "Product Name",
    "description": "Product Description",
    "price": 99.99
  }
