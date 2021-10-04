import pytest
from phonecharge.base import create_app
from phonecharge.models import Recharge, Product, Company, save, delete

import uuid
from datetime import datetime


@pytest.fixture(scope='session')
def app():
    return create_app()


# "id": "id_da_recarga",
# "created_at": "2019-02-01T13:00:00.000Z",
# "company_id": "claro_11",
# "product_id": "claro_10",
# "phone_number": "5511999999999",
# "value": 10.00


@pytest.fixture(scope='session')
def db():
    uid_recharge_1 = uuid.uuid4().int
    uid_recharge_1 = uuid.uuid4().int
    create_at = datetime.isoformat(datetime.now())
    company = [
        Company(id = 1, name = "claro"),
        Company(id = 2, name = "tim")
    ]
    save(company)

    product = [
        Product(id = 1, public_id = "claro_10", company_id = 1, value = "10.0"),
        Product(id = 2, public_id = "claro_20", company_id = 1, value = "20.0"),
        Product(id = 3, public_id = "tim_10", company_id = 2, value = "10.0"),
        Product(id = 4, public_id = "tim_20", company_id = 2, value = "20.0"),
    ]
    save(product)

    recharge = [
        Recharge(id = 1, public_id = uid_recharge_1, company_id = 2, product_id = "tim_10", create_at=create_at, value = "10.0", phone_number="5511999999999"),
        Recharge(id = 2, public_id = uid_recharge_2, company_id = 1, product_id = "claro_20", create_at=create_at,  value = "20.0", phone_number="5511969999999"),
    ]

    save(recharge)
    db_session.commit()
    yield company, product, recharge
    delete(company)
    delete(product)
    delete(recharge)


