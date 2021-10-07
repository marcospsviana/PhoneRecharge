import uuid

import pytest

from phonecharge.base import create_app

# from phonecharge.db.db_operations import save, delete
from phonecharge.models import Company, Product, Recharge


@pytest.fixture(scope="session")
def app():
    return create_app()


@pytest.fixture(scope="session")
def db():
    uid_recharge_1 = str(uuid.uuid4().int)
    uid_recharge_2 = str(uuid.uuid4().int)

    companies = [
        Company(public_id="claro_11", name="claro"),
        Company(public_id="tim_11", name="tim"),
    ]
    for company in companies:
        company.save()

    products = [
        Product(public_id="claro_10", company_id="claro_11", value=10.0),
        Product(public_id="claro_20", company_id="claro_11", value=20.0),
        Product(public_id="tim_10", company_id="tim_11", value=10.0),
        Product(public_id="tim_20", company_id="tim_11", value=20.0),
    ]
    for product in products:
        product.save()

    recharges = [
        Recharge(
            public_id=uid_recharge_1,
            product_id="tim_10",
            phone_number="5511999999999",
            value=10.0,
        ),
        Recharge(
            public_id=uid_recharge_2,
            product_id="claro_20",
            phone_number="5511969999999",
            value=20.0,
        ),
    ]

    for recharge in recharges:
        recharge.save()

    yield products, recharges, companies

    for recharge in recharges:
        recharge.delete()

    for product in products:
        product.delete()

    for company in companies:
        company.delete()
