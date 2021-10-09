from flask_restful import Resource
from phonecharge.models import get_products
from flask import request


class CompanyProducts(Resource):
    def get(self):
        company_id = request.args.get("company_id")
        products = get_products(company_id)
        product = [
            {
                "id": product_single.public_id,
                "company": product_single.Company.public_id,
                "value": product_single.value,
            }
            for product_single in products
        ]
        print(f"product response {product}")

        return product
