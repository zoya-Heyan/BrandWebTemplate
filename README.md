# 我的品牌 - 电商网站

一个基于 Flask 开发的电商网站，展示和销售汽车模型产品。

## 功能特性

- 🏠 **首页** - 展示产品轮播和精选商品
- 🛍️ **产品列表** - 浏览所有可用产品
- 📦 **产品详情** - 查看产品详细信息并添加到购物车
- 🛒 **购物车** - 管理购物车商品，查看总价
- 📖 **关于我们** - 了解品牌信息
- 📩 **联系我们** - 提交留言表单

## 技术栈

- **后端框架**: Flask
- **前端**: HTML, CSS, JavaScript
- **模板引擎**: Jinja2 (Flask 内置)

## 安装与运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置密钥

在 `app.py` 中修改 `secret_key`：

```python
app.secret_key = "your_secret_key_here"  # 请换成你自己的安全密钥
```

### 3. 运行应用

```bash
python app.py
```

应用将在 `http://127.0.0.1:5000` 启动（调试模式）。

## 项目结构

```
myweb-main/
├── app.py                 # Flask 应用主文件
├── requirements.txt       # Python 依赖
├── templates/            # HTML 模板
│   ├── base.html        # 基础模板
│   ├── index.html       # 首页
│   ├── products.html    # 产品列表
│   ├── product_detail.html  # 产品详情
│   ├── cart.html        # 购物车
│   ├── about.html       # 关于我们
│   └── contact.html     # 联系我们
└── static/              # 静态资源
    ├── css/
    │   └── style.css    # 样式文件
    └── images/          # 图片资源
        ├── logo.png
        ├── product1.jpg
        ├── product2.jpg
        ├── product3.jpg
        └── slide*.jpg
```

## 路由说明

- `/` - 首页
- `/products` - 产品列表页
- `/product/<product_id>` - 产品详情页
- `/add_to_cart/<product_id>` - 添加商品到购物车
- `/cart` - 购物车页面
- `/about` - 关于我们
- `/contact` - 联系我们（支持 GET 和 POST）

## 购物车功能

购物车使用 Flask 的 `session` 来存储数据，支持：
- 添加商品到购物车
- 查看购物车商品数量（右上角购物车图标显示）
- 计算购物车总价

## 注意事项

- 开发模式下 `debug=True`，生产环境请设置为 `False`
- 请务必修改 `secret_key` 为安全的随机字符串
- 产品图片需要放在 `static/images/` 目录下

## 许可证

本项目仅供学习和参考使用。

