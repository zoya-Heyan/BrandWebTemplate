from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # 请换成你自己的安全密钥

# 产品数据（图片放在 static/images/ 目录）
products = [
    {
        "id": 1,
        "name": "法拉利488",
        "description": "这是我们的一款高品质产品，采用树脂材料，设计精妙，细节清晰。",
        "image": "product1.jpg",
        "price": "899"
    },
    {
        "id": 2,
        "name": "迈凯伦f1",
               "description": "这款产品注重细节，采用多层喷漆工艺，制作复杂。",
        "image": "product2.jpg",
        "price": "1299"
    },
    {
        "id": 3,
        "name": "兰博基尼毒药",
        "description": "刻线清晰，采用六个模块组装工艺。",
        "image": "product3.jpg",
        "price": "999"
    }
]

@app.context_processor
def cart_item_count():
    cart = session.get('cart', {})
    count = sum(cart.values())
    return dict(cart_count=count)

@app.route("/")
def home():
    return render_template("index.html", products=products)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def product_list():
    return render_template("products.html", products=products)

@app.route("/product/<int:product_id>", methods=["GET", "POST"])
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "找不到该产品", 404

    if request.method == "POST":
        cart = session.get("cart", {})
        cart[str(product_id)] = cart.get(str(product_id), 0) + 1
        session["cart"] = cart
        return redirect(url_for("cart"))

    return render_template("product_detail.html", product=product)

@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    cart = session.get("cart", {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/cart")
def cart():
    cart = session.get("cart", {})
    cart_items = []
    total_price = 0
    for pid_str, qty in cart.items():
        pid = int(pid_str)
        product = next((p for p in products if p["id"] == pid), None)
        if product:
            price_num = int(product["price"])
            subtotal = price_num * qty
            total_price += subtotal
            cart_items.append({
                "product": product,
                "quantity": qty,
                "subtotal": subtotal
            })
    return render_template("cart.html", cart_items=cart_items, total_price=total_price)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        message = request.form["message"]
        print(f"收到留言：姓名={name}, 内容={message}")
        return render_template("contact.html", success=True, name=name)
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)