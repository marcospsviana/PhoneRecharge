from phonecharge.models import Product, Recharge, Company, session
from datetime import datetime


def product(id=None):
    if id is not None:
        products = (
            session.query(Company, Product.public_id, Product.value)
            .join(Company)
            .filter(Company.public_id == id)
            .all()
        )
        return {
            "company_id": f"{id}",
            "products": [
                {"id": product.public_id, "value": product.value}
                for product in products
            ],
        }
    else:
        products_all = session.query(Product).all()
        company_all = session.query(Company).all()

        list_all = [
            {
                "company_id": f"{company.public_id}",
                "products": [
                    {"id": product.public_id, "value": product.value}
                    for product in products_all
                    if product.company_id == company.id
                ],
            }
            for company in company_all
        ]

        return list_all


def recharge(phone_number=None, public_id=None):
    if phone_number is not None:
        recharge = (
            session.query(
                Recharge.value,
                Recharge.public_id,
                Recharge.created_at,
                Recharge.product_id,
                Recharge.phone_number,
            )
            .filter(Recharge.phone_number == phone_number)
            .first()
        )

        return {
            "id": recharge.public_id,
            "created_at": f"{datetime.isoformat(recharge.created_at)}",
            "company_id": f"{session.query(Company.public_id).filter(Product.id == recharge.product_id).first()[0]}",
            "product_id": f"{session.query(Product.public_id).filter(Product.id == recharge.product_id).first()[0]}",
            "phone_number": recharge.phone_number,
            "value": recharge.value,
        }
    elif public_id is not None:
        recharge = (
            session.query(
                Recharge.value,
                Recharge.public_id,
                Recharge.created_at,
                Recharge.product_id,
                Recharge.phone_number,
            )
            .filter(Recharge.public_id == public_id)
            .first()
        )

        return {
            "id": recharge.public_id,
            "created_at": f"{datetime.isoformat(recharge.created_at)}",
            "company_id": f"{session.query(Company.public_id).filter(Product.id == recharge.product_id).first()[0]}",
            "product_id": f"{session.query(Product.public_id).filter(Product.id == recharge.product_id).first()[0]}",
            "phone_number": recharge.phone_number,
            "value": recharge.value,
        }
    else:
<<<<<<< HEAD
=======
        products_all = session.query(Product).all()
        company_all = session.query(Company).all()
>>>>>>> e49233b5e41b7288d9f2f1948c1c6826b0fe6f3e
        recharge_all = session.query(
            Recharge.public_id,
            Recharge.created_at,
            Recharge.phone_number,
            Recharge.product_id,
            Recharge.value,
        ).all()

        recharge_list = [
            {
                "id": recharge.public_id,
                "created_at": f"{datetime.isoformat(recharge.created_at)}",
                "company_id": f"{session.query(Company.public_id).filter(Product.id == recharge.product_id).first()[0]}",
                "product_id": f"{session.query(Product.public_id).filter(Product.id == recharge.product_id).first()[0]}",
                "phone_number": recharge.phone_number,
                "value": recharge.value,
            }
            for recharge in recharge_all
        ]

        return recharge_list
<<<<<<< HEAD
=======

>>>>>>> e49233b5e41b7288d9f2f1948c1c6826b0fe6f3e
