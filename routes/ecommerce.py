from flask import Blueprint, render_template
from routes.cache_file import cache


ecommerce_page = Blueprint('ecommerce', __name__, template_folder='../static/templates/', static_folder='static')

'''
ROUTES:
home
login
logout
register
explore
checkout
product
profile
api for explore
api for product images
'''

@ecommerce_page.route('/ecommerce', methods=['GET'])
@cache.cached()
def ecommerce_home():
    response = render_template('index.html'), 200
    return response


@ecommerce_page.route('/ecommerce/login', methods=['GET'])
@cache.cached()
def ecommerce():
    response = render_template('login.html'), 200
    return response


@ecommerce_page.route('/ecommerce/login', methods=['POST'])
@cache.cached()
def ecommerce_validation():
    response = render_template('index.html'), 200
    return response


@ecommerce_page.route('/ecommerce/logout', methods=['GET'])
@cache.cached()
def ecommerce_logout():
    response = render_template('index.html'), 200
    return response


@ecommerce_page.route('/ecommerce/register', methods=['GET'])
@cache.cached()
def ecommerce_register():
    response = render_template('register.html'), 200
    return response


@ecommerce_page.route('/ecommerce/register', methods=['POST'])
@cache.cached()
def ecommerce_register_validation():
    response = render_template('profile.html'), 200
    return response


@ecommerce_page.route('/ecommerce/explore', methods=['GET'])
@cache.cached()
def ecommerce_explore():
    response = render_template('explore.html'), 200
    return response


@ecommerce_page.route('/ecommerce/checkout', methods=['GET'])
@cache.cached()
def ecommerce_checkout():
    response = render_template('checkout.html'), 200
    return response


@ecommerce_page.route('/ecommerce/profile', methods=['GET'])
@cache.cached()
def ecommerce_profile():
    response = render_template('profile.html'), 200
    return response


@ecommerce_page.route('/ecommerce/profile', methods=['POST'])
@cache.cached()
def ecommerce_profile_edit():
    response = render_template('profile.html'), 200
    return response


@ecommerce_page.route('/ecommerce/api/<id>', methods=['GET'])
@cache.cached()
def ecommerce(id: int):
    pass

