from flask_restful import Resource, output_json
from phonecharge.models import Product, Recharge, get_products
from flask import request




class CompanyProducts(Resource):
    def get(self):
        if request.args.get('company_id'):
            company_id = request.args.get('company_id')
        else:
            company_id = None
        products = get_products(company_id)
        
        return products
    

class CompanyProductsCreate(Resource):
    def post(self):
        product_data = request.data
        product = Product(product_data[''])


