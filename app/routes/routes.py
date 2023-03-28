from app import app
from app.controllers import default

# Is Alive ?
app.add_url_rule('/', 'index', default.index)

# Deliverer
app.add_url_rule('/read/deliverer', 'listDeliverers', default.listDeliverers, methods=['GET'])
app.add_url_rule('/create/deliverer', 'createDeliverer', default.createDeliverer, methods=['POST'])
app.add_url_rule('/update/deliverer', 'editDeliverer', default.editDeliverer, methods=['PUT'])
app.add_url_rule('/delete/deliverer/<id>', 'deleteDeliverer', default.deleteDeliverer, methods=['DELETE'])

# Customer
app.add_url_rule('/read/customer', 'listCustomers', default.listCustomers, methods=['GET'])
app.add_url_rule('/create/customer', 'createCustomer', default.createCustomer, methods=['POST'])
app.add_url_rule('/update/customer', 'editCustomer', default.editCustomer, methods=['PUT'])
app.add_url_rule('/delete/customer/<id>', 'deleteCustomer', default.deleteCustomer, methods=['DELETE'])

# Product
app.add_url_rule('/read/product', 'listProducts', default.listProducts, methods=['GET'])
app.add_url_rule('/create/product', 'createProduct', default.createProduct, methods=['POST'])
app.add_url_rule('/update/product', 'editProduct', default.editProduct, methods=['PUT'])
app.add_url_rule('/delete/product/<id>', 'deleteProduct', default.deleteProduct, methods=['DELETE'])