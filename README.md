# E-Commerce Website - Car Models Store

A Flask-based e-commerce website for displaying and selling car model products.

## Features

- 🏠 **Home Page** - Product carousel and featured items
- 🛍️ **Product List** - Browse all available products
- 📦 **Product Details** - View detailed product information and add to cart
- 🛒 **Shopping Cart** - Manage cart items and view total price
- 📖 **About Us** - Learn about the brand
- 📩 **Contact** - Submit contact form messages

## Tech Stack

- **Backend Framework**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **Template Engine**: Jinja2 (built-in with Flask)

## Installation & Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Secret Key

Update the `secret_key` in `app.py`:

```python
app.secret_key = "your_secret_key_here"  # Replace with your own secure secret key
```

### 3. Run the Application

```bash
python app.py
```

The application will start at `http://127.0.0.1:5000` (debug mode enabled).

## Project Structure

```
myweb-main/
├── app.py                 # Flask application main file
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   ├── products.html    # Product list
│   ├── product_detail.html  # Product details
│   ├── cart.html        # Shopping cart
│   ├── about.html       # About us
│   └── contact.html     # Contact form
└── static/              # Static resources
    ├── css/
    │   └── style.css    # Stylesheet
    └── images/          # Image assets
        ├── logo.png
        ├── product1.jpg
        ├── product2.jpg
        ├── product3.jpg
        └── slide*.jpg
```

## Routes

- `/` - Home page
- `/products` - Product list page
- `/product/<product_id>` - Product detail page
- `/add_to_cart/<product_id>` - Add product to cart
- `/cart` - Shopping cart page
- `/about` - About us page
- `/contact` - Contact page (supports GET and POST)

## Shopping Cart Functionality

The shopping cart uses Flask's `session` to store data and supports:
- Adding products to cart
- Viewing cart item count (displayed on cart icon in top right)
- Calculating total cart price

## Products

The application currently features three car model products:
- Ferrari 488
- McLaren F1
- Lamborghini Veneno

Product data is stored in the `products` list in `app.py`. Each product includes:
- ID
- Name
- Description
- Image filename
- Price

## Important Notes

- Debug mode is enabled (`debug=True`) - set to `False` for production
- **Important**: Change the `secret_key` to a secure random string before deploying
- Product images should be placed in the `static/images/` directory
- The contact form currently prints messages to console (can be extended to send emails or save to database)

## License

This project is for learning and reference purposes only.

