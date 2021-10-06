import pytest
from phonecharge.base import create_app
from phonecharge.models import (
    save_company,
    save_products,
    save_recharge,
    delete,
    get_products,
    get_companies,
    get_recharges,
)

import uuid


@pytest.fixture(scope="session")
def app():
    return create_app()


@pytest.fixture(scope="session")
def db():
    uid_recharge_1 = str(uuid.uuid4().int)
    uid_recharge_2 = str(uuid.uuid4().int)

    save_company("claro_11", "claro")
    save_company("tim_11", "tim")

    save_products("claro", "claro_10", 10.0)
    save_products("claro", "claro_20", 20.0)
    save_products("tim", "tim_10", 10.0)
    save_products("tim", "tim_20", 20.0)

    save_recharge(uid_recharge_1, "tim_10", "5511999999999", 10.0)
    save_recharge(uid_recharge_2, "claro_20", "5511969999999", 20.0)

    products = get_products()
    recharges = get_recharges()
    companies = get_companies()
    yield products, recharges, companies

    delete("recharges", uid_recharge_1)
    delete("recharges", uid_recharge_2)

    delete("products", "claro_10")
    delete("products", "claro_20")
    delete("products", "tim_10")
    delete("products", "tim_20")

    delete("companies", "claro_11")
    delete("companies", "tim_11")
