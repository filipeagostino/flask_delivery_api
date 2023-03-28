from app import app, mysql
from flask import make_response, jsonify, request, json
from app.tools import cpf_validator, cepvalidator
from colorama import Fore, init
init(autoreset=True)

# Index

def index():
    return "<h1>Flask Apllication Begin's!</h1>"


# Deliverers


# List Deliverer
def listDeliverers():
    my_cursor = mysql.cursor()
    my_cursor.execute('SELECT * FROM deliverer')
    deliverers = my_cursor.fetchall()

    print(Fore.YELLOW + f'Deliverers: {deliverers}')

    if deliverers:
        return make_response(
            jsonify(
                message='Deliverer list!',
                data=deliverers
            )
        )
    
    else:
        return make_response(
            jsonify(
                {'message': 'Sorry, Deliverers not found!'}
            )
        ), 404


# Add New Deliverer

def createDeliverer():
    deliverer = request.json
    print(Fore.YELLOW + f'Deliverer Received: {deliverer}')

    my_cursor = mysql.cursor()

    find = f"SELECT * FROM deliverer WHERE (cpf='{deliverer['cpf']}')"
    
    my_cursor.execute(find)
    result = my_cursor.fetchall()
    print(Fore.YELLOW + f'SQL Result: {result}')

    if result:
        return make_response(
            jsonify(
                {'message': 'Sorry, Cpf number already Added!'}
            )
        ), 409
    
    check_cpf = cpf_validator.Cpfvalidator(deliverer['cpf'])
    validation = check_cpf.test()

        
    if validation == True:

        insert = f"INSERT INTO deliverer (name, email, cpf, phone) VALUES ('{deliverer['name']}', '{deliverer['email']}', '{deliverer['cpf']}', '{deliverer['phone']}')"

        my_cursor.execute(insert)
        mysql.commit()

        return make_response(
            jsonify(
                message='Deliverer Added!',
                data=deliverer)
        ), 201

    else:
        return make_response(
            jsonify(
                {'message': 'Sorry, Cpf number is invalid!'}
            )
        ), 400


# Edit Deliverer
def editDeliverer():
    deliverer = request.json

    my_cursor = mysql.cursor()

    find = f"SELECT * FROM deliverer WHERE (id='{deliverer['id']}')"

    my_cursor.execute(find)
    result = my_cursor.fetchall()

    print(Fore.YELLOW + f'SQL Result: {result}')

    if result:
        
        check_cpf = cpf_validator.Cpfvalidator(deliverer['cpf'])
        validation = check_cpf.test()

        if validation == True:
            update = f"UPDATE deliverer SET email='{deliverer['email']}', cpf='{deliverer['cpf']}', phone='{deliverer['phone']}' WHERE id=('{result[0][0]}')"
            my_cursor.execute(update)
            mysql.commit()

            my_cursor.execute(find)
            deliverer = my_cursor.fetchall()

            return make_response(
                jsonify(
                    messagem='Deliverer Altered!',
                    data=deliverer
                )
            )
        else:
            return make_response(
            jsonify(
                {'message': 'Sorry, Cpf number is invalid!'}
            )
        ), 400
    
    else:
        return make_response(
            {'message': 'Sorry, Deliverer not found!'}
        ), 404

# Delete Deliverer


def deleteDeliverer(id):
    deliverer_id = id

    my_cursor = mysql.cursor()

    find = f"SELECT * FROM deliverer WHERE (id='{deliverer_id}')"
    
    my_cursor.execute(find)
    result = my_cursor.fetchall()

    if result:
        
        delete = f"DELETE FROM deliverer WHERE (id='{deliverer_id}')"
        my_cursor.execute(delete)
        mysql.commit()

        return {'Message': 'Deliverer deleted!'}, 200

    else:
        return {'Message': 'Sorry, deliverer not found!'}, 404


# Customers


# List Customer

def listCustomers():
    my_cursor = mysql.cursor()
    my_cursor.execute('SELECT * FROM customer')
    customers = my_cursor.fetchall()

    print(Fore.YELLOW + f'Customers: {customers}')

    if customers:
        return make_response(
            jsonify(
                message='Costumer list!',
                data=customers
            )
        )
    
    else:
        return make_response(
            jsonify(
                {'message': 'Sorry, Customers not found!'}
            )
        ), 404

# Add New Customer

def createCustomer():
    customer = request.json
    print(Fore.YELLOW + f'Customer Received: {customer}')

    my_cursor = mysql.cursor()

    find = f"SELECT * FROM customer WHERE (cpf='{customer['cpf']}')"
    
    my_cursor.execute(find)
    result = my_cursor.fetchall()
    print(Fore.YELLOW + f'SQL Result: {result}')

    if result:
        return make_response(
            jsonify(
                {'message': 'Sorry, Cpf number already Added!'}
            )
        ), 409
    
    
    check_cpf = cpf_validator.Cpfvalidator(customer['cpf'])
    cpf_validation = check_cpf.test()

    print(Fore.YELLOW + f'CPF VALIDATION: {cpf_validation}')

    if cpf_validation == False:
        return make_response(
            jsonify(
                {'message': 'Sorry, Cpf number is invalid!'}
            )
        ), 409

    
    cep_validation = cepvalidator.cepValidator(customer['zip_code'])

    if cep_validation == False:    
        return make_response(
            jsonify(
                {'message': 'Sorry, Zip code is invalid!'}
            )
        ), 409
    
    else:
        insert = f"INSERT INTO customer (name, zip_code, house_number, cpf, email, phone) VALUES ('{customer['name']}', '{customer['zip_code']}', '{customer['house_number']}', '{customer['cpf']}', '{customer['email']}', '{customer['phone']}')"

        my_cursor.execute(insert)
        mysql.commit()

        return make_response(
            jsonify(
                message='Customer Added!',
                data=customer)
        ), 201


# Edit Customer

def editCustomer():
    customer = request.json
    print(Fore.YELLOW + f'Customer Received: {customer}')

    my_cursor = mysql.cursor()

    find = f"SELECT * FROM customer WHERE (id='{customer['id']}')"
    
    my_cursor.execute(find)
    result = my_cursor.fetchall()
    print(Fore.YELLOW + f'SQL Result: {result}')
    print(f'result: {result[0][4]}, cpf: {customer["cpf"]}')
    
    if result[0][5] == customer['cpf']:
        return make_response(
            jsonify(
                {'message': 'Sorry, Cpf number already Added!'}
            )
        ), 409

    if not result:
        return make_response(
            jsonify(
                {'message': 'Sorry, Customer not found!'}
            )
        ), 404
    
    search = f"SELECT * FROM customer WHERE (cpf='{customer['cpf']}')"
    
    my_cursor.execute(search)
    search_result = my_cursor.fetchall()

    if search_result:
        return make_response(
            jsonify(
                {'message': 'Sorry, Cpf number already Added!'}
            )
        ), 409

    check_cpf = cpf_validator.Cpfvalidator(customer['cpf'])
    cpf_validation = check_cpf.test()

    if cpf_validation == False:
        return make_response(
            jsonify(
                {'message': 'Sorry, Cpf number is invalid!'}
            )
        ), 409

    cep_validation = cepvalidator.cepValidator(customer['zip_code'])

    if cep_validation == False:    
        return make_response(
            jsonify(
                {'message': 'Sorry, Zip code is invalid!'}
            )
        ), 409

    else:
        update = f"UPDATE customer SET name='{customer['name']}', zip_code='{customer['zip_code']}', house_number='{customer['house_number']}', cpf='{customer['cpf']}', email='{customer['email']}', phone='{customer['phone']}' WHERE id=('{result[0][0]}')"
        my_cursor.execute(update)
        mysql.commit()

        return make_response(
            jsonify(
                message='Customer Updated!',
                data=customer)
        ), 201

        
# Delete Customer

def deleteCustomer(id):
    my_cursor = mysql.cursor()

    find = f"SELECT * FROM customer WHERE (id='{id}')"
    
    my_cursor.execute(find)
    result = my_cursor.fetchall()

    if result:
        
        delete = f"DELETE FROM customer WHERE (id='{id}')"
        my_cursor.execute(delete)
        mysql.commit()

        return make_response(
            jsonify(
                message='Customer Deleted!',
                data=result)
        )

    else:
        return {'Message': 'Sorry, customer not found!'}, 404


# Products


# List Products

def listProducts():
    my_cursor = mysql.cursor()
    my_cursor.execute('SELECT * FROM product')
    products = my_cursor.fetchall()

    print(Fore.YELLOW + f'Products: {products}')

    if products:
        return make_response(
            jsonify(
                message='Product list!',
                data=products
            )
        )
    
    else:
        return make_response(
            jsonify(
                {'message': 'Sorry, Products not found!'}
            )
        ), 404

# Add New Products
def createProduct():
    product = request.json

    print(Fore.YELLOW + f'Product Received: {product}')
    
    my_cursor = mysql.cursor()

    find = f"SELECT * FROM product WHERE (product_name='{product['product_name']}')"
    
    my_cursor.execute(find)
    result = my_cursor.fetchall()
    print(Fore.YELLOW + f'SQL Result: {result}')

    if result:
        return make_response(
            jsonify(
                {'message': 'Sorry, Product already Added!'}
            )
        ), 409
    else:
        if not status:
            product['delivery_status'] = 'transport'
        
        insert = f"INSERT INTO product (deliverer, customer, product_name, delivery_status) VALUES ('{product['deliverer']}', '{product['customer']}', '{product['product_name']}', '{product['delivery_status']}')"

        my_cursor.execute(insert)
        mysql.commit()

        return make_response(
            jsonify(
                message='Product Added!',
                data=product)
        ), 201

# Edit Products

def editProduct():
    product = request.json

    my_cursor = mysql.cursor()

    find = f"SELECT * FROM product WHERE (id='{product['id']}')"

    my_cursor.execute(find)
    result = my_cursor.fetchall()

    print(Fore.YELLOW + f'SQL Result: {result}')    
    
    if not result:
        return make_response(
            jsonify(
                {'message': 'Sorry, Product not found!'}
            )
        ), 404
    
    else:
        update = f"UPDATE product SET deliverer='{product['deliverer']}', customer='{product['customer']}', product_name='{product['product_name']}', delivery_status='{product['delivery_status']}' WHERE id=('{result[0][0]}')"
        my_cursor.execute(update)
        mysql.commit()

        return make_response(
            jsonify(
                message='Product Updated!',
                data=product)
        ), 201


# Delete Products

def deleteProduct(id):
    my_cursor = mysql.cursor()

    find = f"SELECT * FROM product WHERE (id='{id}')"
    
    my_cursor.execute(find)
    result = my_cursor.fetchall()

    if result:
        
        delete = f"DELETE FROM product WHERE (id='{id}')"
        my_cursor.execute(delete)
        mysql.commit()

        return make_response(
            jsonify(
                message='Product Deleted!',
                data=result)
        )

    else:
        return {'Message': 'Sorry, product not found!'}, 404