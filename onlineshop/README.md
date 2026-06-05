# Online Shop

A Django-based e-commerce application for browsing and managing computer components and electronics.

#### README been created with AI

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Setup & Configuration](#setup--configuration)
- [Django Admin Site](#django-admin-site)
- [Usage](#usage)
- [Models](#models)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)

## Overview

Online Shop is a fully-functional Django web application designed to demonstrate modern e-commerce practices. The application allows users to browse products by category and brand, view detailed product information, and manage inventory through an intuitive admin interface. Built with Django 6.0.4 and Python 3.13+, it showcases best practices in model design, URL routing, and template rendering.

## Features

- 🛍️ **Product Catalog**: Browse products organized by categories and brands
- 🏷️ **Category Management**: Filter products by categories (Graphics Cards, CPUs, RAM, etc.)
- 🏢 **Brand Management**: View products from different manufacturers
- 📸 **Product Images**: Display product images with fallback placeholder support
- 📊 **Dynamic Content**: Real-time product count and inventory tracking
- 👤 **User Authentication**: Login/logout functionality for registered users
- 🔐 **Admin Interface**: Comprehensive Django admin site for content management
- 📱 **Responsive Design**: Clean, accessible interface for browsing

## Project Structure

```
onlineshop/
├── pyproject.toml                 # Project configuration and dependencies
├── README.md                       # This file
├── db.sqlite3                      # SQLite database (production/development)
├── manage.py                       # Django management script
├── catalog/                        # Main Django app
│   ├── migrations/                # Database migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_category_name_and_more.py
│   │   ├── 0003_alter_product_description.py
│   │   ├── 0004_alter_category_name_brand_product_brand.py
│   │   ├── 0005_alter_product_brand.py
│   │   ├── 0006_product_image.py
│   │   ├── 0007_alter_product_image.py
│   │   └── 0008_alter_product_image.py
│   ├── static/                    # Static files
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── images/               # Static images
│   ├── templates/                 # HTML templates
│   │   ├── base_generic.html      # Base template
│   │   ├── catalog/               # Catalog templates
│   │   │   ├── index.html
│   │   │   ├── product_list.html
│   │   │   ├── product_detail.html
│   │   │   ├── brand_list.html
│   │   │   └── brand_detail.html
│   │   └── registration/          # Auth templates
│   │       ├── login.html
│   │       ├── logged_out.html
│   │       ├── password_reset_form.html
│   │       ├── password_reset_done.html
│   │       ├── password_reset_confirm.html
│   │       └── password_reset_complete.html
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py                    # App configuration
│   ├── models.py                  # Data models
│   ├── tests.py                   # Unit tests
│   ├── urls.py                    # URL routing
│   └── views.py                   # View logic
├── media/                         # User-uploaded files
│   └── products/                  # Product images
└── onlineshop/                    # Django project settings
    ├── __init__.py
    ├── settings.py                # Django settings
    ├── urls.py                    # Main URL configuration
    ├── asgi.py                    # ASGI configuration
    └── wsgi.py                    # WSGI configuration
```

## Prerequisites

- **Python**: 3.13 or higher
- **pip**: Python package manager
- **Git**: For version control (optional)
- **Virtual Environment**: Recommended (venv, virtualenv, or Poetry)

## Installation

### 1. Clone the Repository

```bash
cd /Users/djoni1vincent/dev/Django/django-shopping-site/onlineshop
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
# or using pyproject.toml:
pip install -e .
```

The project requires:

- **django** ≥ 6.0.4 - Web framework
- **django-stubs** ≥ 6.0.3 - Type hints for Django
- **pillow** ≥ 12.2.0 - Image processing library

## Setup & Configuration

### 1. Apply Database Migrations

Run all pending migrations to set up the database schema:

```bash
python manage.py migrate
```

This will create the necessary tables for Products, Categories, Brands, and Django's built-in models.

### 2. Create a Superuser Account

Create an administrative user account to access the Django admin site:

```bash
python manage.py createsuperuser
```

You will be prompted to enter:

- **Username**: Your admin username (e.g., `admin`)
- **Email**: Your email address
- **Password**: A strong password (must confirm)

Example:

```
Username: admin
Email: admin@example.com
Password: ••••••••••
Password (again): ••••••••••
Superuser created successfully.
```

### 3. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The application will be available at: `http://127.0.0.1:8000/`

### 4. Access the Admin Site

Navigate to the admin interface:

```
http://127.0.0.1:8000/admin
```

Login with your superuser credentials created in Step 2.

## Django Admin Site

### Overview

The Django Admin Site is a powerful tool for managing your application's data. It automatically generates a user-friendly interface based on your models, allowing you to create, read, update, and delete (CRUD) records without writing additional code.

### Admin Site Features

#### Model Registration

All models are registered in `catalog/admin.py`:

```python
from django.contrib import admin
from .models import Product, Category, Brand

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'stock')
    list_filter = ('category', 'brand', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
```

#### Key Admin Features

**List View Enhancements**:

- **list_display**: Show multiple fields in the list view
- **list_filter**: Add sidebar filters for quick filtering
- **search_fields**: Enable search functionality

**Detail View Customization**:

- **fieldsets**: Organize fields into grouped sections
- **fields**: Control which fields are displayed and their order
- **readonly_fields**: Mark fields as read-only

**Inline Editing**:

- Manage related records (e.g., edit products while viewing a brand)

### Managing Content Through Admin

#### Adding a New Product

1. Navigate to **Admin Site** → **Products**
2. Click **+ Add Product** button
3. Fill in the following fields:
   - **Name**: Product name
   - **Brand**: Select from dropdown
   - **Price**: Enter decimal price
   - **Stock**: Quantity available
   - **Description**: Product details
   - **Category**: Select category
   - **Image**: Upload product image (optional)
4. Click **Save** to create the product

#### Editing Existing Products

1. Go to **Admin Site** → **Products**
2. Click on a product name to edit
3. Modify the desired fields
4. Click **Save** to update

#### Deleting Products

1. In the products list, select products by checking the checkbox
2. Select "Delete selected [items]" from the Action dropdown
3. Confirm deletion

#### Filtering & Searching

The admin list view provides:

- **Filter Sidebar**: Filter by Category, Brand, or Creation Date
- **Search Box**: Search products by name or description

### Advanced Admin Configuration

#### Product Admin Configuration

```python
class ProductAdmin(admin.ModelAdmin):
    # Display these fields in list view
    list_display = ('name', 'brand', 'category', 'price', 'stock', 'image_url')

    # Add filters on the right sidebar
    list_filter = ('category', 'brand', 'created_at')

    # Enable search by these fields
    search_fields = ('name', 'description')

    # Order list by creation date (newest first)
    ordering = ('-created_at',)
```

#### Brand Admin Configuration

```python
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_count')
    search_fields = ('name',)

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Number of Products'
```

#### Category Admin Configuration

```python
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_count')

    def product_count(self, obj):
        return obj.products.count()
    product_count.short_description = 'Products in Category'
```

## Usage

### Accessing the Frontend

**Home Page**: `http://127.0.0.1:8000/`

- Displays welcome message
- Shows record counts for Products, Categories, and Brands
- Visit counter

**Products List**: `http://127.0.0.1:8000/products/`

- Browse all available products
- View product images, names, and prices
- Click to view detailed product information

**Product Detail**: `http://127.0.0.1:8000/products/<id>/`

- View complete product information
- Display product image
- Show stock availability

**Brands List**: `http://127.0.0.1:8000/brands/`

- View all available brands
- See products associated with each brand

**Brand Detail**: `http://127.0.0.1:8000/brands/<id>/`

- View brand information
- Browse products from specific brand

**Authentication**:

- **Login**: `http://127.0.0.1:8000/accounts/login/`
- **Logout**: `http://127.0.0.1:8000/accounts/logout/`
- **Password Reset**: `http://127.0.0.1:8000/accounts/password_reset/`

## Models

### Product Model

```python
class Product(models.Model):
    name = CharField(max_length=100)          # Product name
    brand = ForeignKey(Brand)                 # Associated brand
    price = DecimalField()                    # Price with 2 decimal places
    stock = PositiveIntegerField()            # Quantity in stock
    description = TextField(max_length=1000)  # Product description
    category = ForeignKey(Category)           # Product category
    image = ImageField(upload_to='products')  # Product image
    created_at = DateTimeField()              # Creation timestamp
    updated_at = DateTimeField()              # Last update timestamp
```

**Methods**:

- `__str__()`: Returns the product name
- `get_absolute_url()`: Returns the product detail URL
- `image_url` (property): Returns image URL or placeholder

### Category Model

```python
class Category(models.Model):
    name = CharField(max_length=100, unique=True)
    # Constraint: Case-insensitive unique constraint
```

**Methods**:

- `__str__()`: Returns the category name
- `get_absolute_url()`: Returns the category detail URL

### Brand Model

```python
class Brand(models.Model):
    name = CharField(max_length=100, unique=True)
    # Constraint: Case-insensitive unique constraint
```

**Methods**:

- `__str__()`: Returns the brand name
- `get_absolute_url()`: Returns the brand detail URL

## Screenshots

### Home Page

![Online Shop Home Page](https://via.placeholder.com/800x400?text=Home+Page)

- Welcome message
- Dynamic record counts
- Navigation links to products and brands

### Product List

![Product List](https://via.placeholder.com/800x400?text=Product+List)

- Grid of products with images
- Product name, brand, and price
- Stock availability

### Product Detail

![Product Detail](https://via.placeholder.com/800x400?text=Product+Detail)

- Full product information
- High-resolution product image
- Description and specifications
- Stock status and pricing

### Django Admin - Products List

![Admin Products List](https://via.placeholder.com/800x400?text=Admin+Products+List)

- Complete product inventory
- Quick filters by category and brand
- Bulk actions for management

### Django Admin - Add Product

![Admin Add Product](https://via.placeholder.com/800x400?text=Admin+Add+Product)

- Intuitive form for adding new products
- Image upload functionality
- Field validation and help text

## Future Enhancements

### Phase 1: Core Features

- [ ] Shopping cart functionality
- [ ] Order management system
- [ ] User reviews and ratings
- [ ] Wishlist feature
- [ ] Product comparison tool

### Phase 2: Advanced Features

- [ ] Payment gateway integration (Stripe, PayPal)
- [ ] Inventory tracking and notifications
- [ ] Discount codes and promotions
- [ ] Email notifications
- [ ] API endpoints (REST or GraphQL)

### Phase 3: UI/UX Improvements

- [ ] Mobile app version
- [ ] Advanced search filters
- [ ] Product recommendations
- [ ] Dark mode support
- [ ] Accessibility improvements

### Phase 4: Performance & Scale

- [ ] Database optimization
- [ ] Caching implementation
- [ ] CDN integration for images
- [ ] API rate limiting
- [ ] Load balancing

## Deployment

### Production Checklist

Before deploying to production:

1. **Security Settings** (`settings.py`):

   ```python
   DEBUG = False
   ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
   SECRET_KEY = os.environ.get('SECRET_KEY')
   ```

2. **Environment Variables**: Store sensitive data in `.env`

3. **Static Files**: Collect static files for production

   ```bash
   python manage.py collectstatic
   ```

4. **Database**: Use PostgreSQL or MySQL instead of SQLite

5. **Web Server**: Deploy with Gunicorn and Nginx

## Testing

Run tests with:

```bash
python manage.py test
```

View coverage with:

```bash
coverage run --source='.' manage.py test
coverage report
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## References

- [Django Official Documentation](https://docs.djangoproject.com/)
- [Django Admin Site Guide](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Admin_site)
- [Mozilla Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django)
- [Django Models](https://docs.djangoproject.com/en/6.0/topics/db/models/)
- [Django Admin Customization](https://docs.djangoproject.com/en/6.0/ref/contrib/admin/)

## Support

For questions or issues, please open an issue on the repository or contact the development team.

---

**Developer**: Denys
**Last Updated**: June 5, 2026
**Django Version**: 6.0.4+
**Python Version**: 3.13+
