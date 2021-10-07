from flask_restful import Resource, output_json
from phonecharge.models import get_products


class CompanyProducts(Resource):
    def get(self):
        breakpoint()
        products = get_products()
        return output_json(data=products, code=200)
