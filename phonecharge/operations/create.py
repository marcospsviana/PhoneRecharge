from phonecharge.models import Product, Recharge


def save_company(company):
    company_data = Company(company["company_id"], company["id"], company["value"])
    try:
        session.save(product_data)
    except Exception as err:
        return err


def save_product(product):
    product_data = Product(product["company_id"], product["id"], product["value"])
    try:
        session.save(product_data)
    except Exception as err:
        return err


def save_recharge(recharge):
    recharge_data = Recharge(
        recharge["company_id"],
        recharge["product_id"],
        recharge["phone_number"],
        recharge["value"],
    )
    try:
        session.save(recharge_data)
    except Exception as err:
        return err
