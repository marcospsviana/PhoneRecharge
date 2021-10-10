from flask_restful import Resource, output_json
from phonecharge.models import Product, get_products
from flask import request




class CompanyProducts(Resource):
    def get(self):
        if request.args.get('company_id'):
            company_id = request.args.get('company_id')
        else:
            company_id = None
        products = get_products(company_id)
        
        return products

