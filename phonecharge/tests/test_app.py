import json
import pytest


def test_get_root_endpoint(client):
    assert client.get("/").status_code == 404


def test_get_company_endpoint_not_found(client):
    assert client.get("/Company").status_code == 404

def test_get_endpoint_get_company(client, company):
    client.get("/CompanyProducts")
    assert company.public_id == "claro_11"
    assert company.name == "claro"


def test_get_endpoint_products(client, product):
    client.get("/CompanyProducts")
    assert product.public_id == "claro_10"
    assert product.value == 10.0


def test_get_recharge_list_all(client, recharge):
    client.get("/PhoneRecharges")
    assert str(recharge) == "284206977373282501394198671064916751422"


@pytest.mark.parametrize("recharge__phone_number", ["5511999553489"])
def test_get_endpoint_recharge_post(client, recharge):
    payload = json.dumps(
        {"product_id": "claro_20", "phone_number": "5511999553489", "value": 20.00}
    )
    client.post("/PhoneRecharges", data=payload)
    assert recharge.phone_number == "5511999553489"


def test_get_endpoint_get_recharge_by_id(client, recharge):
    client.get("/PhoneRecharges?id=284206977373282501394198671064916751422")
    assert recharge.phone_number == "5511969999999"
    assert recharge.value == 20.0
    assert recharge.product_id == "claro_20"
    assert recharge.created_at == "2021-10-11T21:23:16.220005"
    

def test_user_credentials(client, user):
    assert user.email == "marcospaulo.silvaviana@gmail.com"
    assert user.password == "laylaebel"
    assert user.created_at == "2021-10-12T18:23:16.220005"


@pytest.l
def test_user_credentials_post_(client, user):
    assert user.email == "marcospaulo.silvaviana@gmail.com"
    assert user.password == "laylaebel"
    assert user.created_at == "2021-10-12T18:23:16.220005"

