from werkzeug.exceptions import abort
from flask import render_template
from flask import Blueprint
from app_home.product.models import PRODUCTS
from datetime import datetime

product_blueprint = Blueprint('product', __name__)

@product_blueprint.context_processor
def some_processor():
    def full_name(product):
        return '{0} / {1}'.format(product['category'], product['name'])
    return {'full_name': full_name}

@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
    return render_template('home.html', products=PRODUCTS, timestamp=datetime.now())

@product_blueprint.route('/product/<key>')
def product(key):
    prod = PRODUCTS.get(key)
    if not product:
        abort(404)
    return render_template('product.html', product=prod)

@product_blueprint.app_template_filter('full_name')
def full_name_filter(product):
    return '{0} / {1}'.format(product['category'],
      product['name'])
    
