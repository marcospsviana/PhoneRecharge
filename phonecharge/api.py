from flask_restful import Resource, output_json
from phonecharge.models import Product, Recharge, get_products
from flask import request
from phonecharge.operations import select, create, update




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
        create.save_product(product=request.data)


class Recharge(Resource):
    def get(self):
        if request.args.get('phone_number'):
            recharge = select.recharge(phone_number=request.args.get('phone_number'))
            return recharge
        if request.args.get('id'):
            recharge = select.recharge(public_id==request.args.get('id'))
            return recharge
        else:
            recharge = select.recharge(phone_number=None, public_id=None)
            return recharge
    
    def post(self):
        recharge = create.save_recharge(recharge=request.data)
        return recharge

