from flask_restful import Resource, http_status_message
from phonecharge.models import get_products
from flask import request
from flask_httpauth import HTTPBasicAuth
from passlib.context import CryptContext
from phonecharge.operations import select, create
from phonecharge.models import User, session


auth = HTTPBasicAuth()


@auth.verify_password
def verify(email, password):
    if email and password:
        crypt_context = CryptContext(schemes=["sha256_crypt"])
        result = session.query(User).filter(User.email == email)

        user = {}
        for row in result:
            user["email"] = row.email
            print(f"row password {row.password}")
            user["password"] = row.password
            if crypt_context.verify(password, row.password):
                return user
            else:
                return False
    else:
        http_status_message(401), 401


class CompanyProducts(Resource):
    @auth.login_required
    def get(self):
        if request.args.get("company_id"):
            company_id = request.args.get("company_id")
        else:
            company_id = None
        products = get_products(company_id)

        return products


class Recharge(Resource):
    @auth.login_required
    def get(self):
        if request.args.get("phone_number"):
            recharge = select.recharge(phone_number=request.args.get("phone_number"))
            if recharge == 404:
                return http_status_message(404), 404
            else:
                return recharge
        if request.args.get("id"):
            recharge = select.recharge(public_id=request.args.get("id"))
            if recharge == 404:
                return http_status_message(404), 404
            else:
                return recharge
        else:
            recharge = select.recharge(phone_number=None, public_id=None)
            return recharge

    @auth.login_required
    def post(self):
        recharge = create.save_recharge(recharge=request.data)
        if recharge:
            return http_status_message(201), 201
        else:
            return http_status_message(400)
