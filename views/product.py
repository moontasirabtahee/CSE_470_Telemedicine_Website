from flask import Flask, Blueprint, render_template, request, redirect, url_for
from controllers import create_product, get_all_products, get_product_by_id, update_product

products = Blueprint('products', __name__)

@products.route('/product')
def index():
 
  products = get_all_products()
  product_id = request.args.get('product_id')
  product = None
  edit_mode = False

  if product_id:
    product = get_product_by_id(product_id)
    edit_mode = True

  if request.method == 'POST':
    if edit_mode:
     
      name = request.form.get('name')
      description = request.form.get('description')
      price = float(request.form.get('price'))
      stock = int(request.form.get('stock'))
      update_product(product_id, name, description, price, stock)
      return redirect(url_for('products.html'))
    else:
     
      name = request.form.get('name')
      description = request.form.get('description')
      price = float(request.form.get('price'))
      stock = int(request.form.get('stock'))
      create_product(name, description, price, stock)
      return redirect(url_for('products.html'))

  return render_template('products.html', products=products, product=product, edit_mode=edit_mode)
