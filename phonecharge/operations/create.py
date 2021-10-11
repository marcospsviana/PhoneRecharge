import json
from phonecharge.models import Product, Recharge, Company
import uuid


def save_company(company):
    company_data = Company(public_id=company["company_id"], name=company["name"])
    try:
        company_data.save()
    except Exception as err:
        return err


def save_product(product):
    product_data = Product(product["company_id"], product["id"], product["value"])
    try:
        product_data.save()
    except Exception as err:
        return err


def save_recharge(recharge):
    uid_recharge = str(uuid.uuid4().int)
    print(f"recharge {json.loads(recharge)}")
    recharge = json.loads(recharge)
    recharge_data = Recharge(
        public_id=uid_recharge,
        product_id=recharge["product_id"],
        phone_number=recharge["phone_number"],
        value=recharge["value"],
    )
    try:
        recharge_data.save()
    except Exception as err:
        return err
