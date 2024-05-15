from flask import request, Blueprint

from src.infrastructure.controllers.controller import ProductController  
from src.infrastructure.repositories.mysql_repository import ProductsRepository

repository = ProductsRepository()
controller = ProductController(repository)

product_routes = Blueprint('product_routes', __name__,)

@product_routes.route('/', methods=['GET'])
def get_products():
    return controller.get_products()

@product_routes.route('/<id>', methods=['GET'])
def get_product_by_id(id):
    return controller.get_product_by_id(id)

@product_routes.route('/', methods=['POST'])
def create_product():
    return controller.create_product(request)

@product_routes.route('/<id>', methods=['PUT'])
def update_product(id):
    return controller.update_product(id, request)

@product_routes.route('/<id>', methods=['DELETE'])
def delete_product(id):
    return controller.delete_product(id)