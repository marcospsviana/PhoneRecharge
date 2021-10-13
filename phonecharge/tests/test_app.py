import json
import pytest
from phonecharge.models import Recharge, session


def test_accept_credentials(client, user):
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }
    assert client.get("/PhoneRecharges", headers=headers).status_code == 200


def test_user_credentials(client, user):
    assert user.email == "marcospaulo.silvaviana@gmail.com"
    assert user.password == "laylaebel"
    assert user.created_at == "2021-10-12T18:23:16.220005"


def test_get_debug_false(app):
    assert app.config["DEBUG"] is not True


def test_get_root_endpoint(client):
    assert client.get("/").status_code == 404


def test_get_company_endpoint_not_found(client):
    assert client.get("/Company").status_code == 404


def test_get_endpoint_get_endpoint_products(client, company):
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }
    assert client.get("/CompanyProducts", headers=headers).status_code == 200


def test_get_endpoint_get_endpoint_products_by_company(client, company, app):
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }
    resp = app.test_client().get(
        "/CompanyProducts?id_company=claro_11", headers=headers, data={}
    )
    assert resp.status_code == 200
    assert company.public_id == "claro_11"


def test_get_endpoint_get_company(client, company):
    client.get("/CompanyProducts")
    assert company.public_id == "claro_11"
    assert company.name == "claro"


def test_get_endpoint_products(client, product):
    client.get("/CompanyProducts")
    assert product.public_id == "claro_10"
    assert product.value == 10.0


def test_get_endpoint_products_all_with_login(client, product):
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }
    assert client.get("/CompanyProducts", headers=headers).status_code == 200


def test_get_recharge_list_all(client, recharge):
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }
    assert client.get("/PhoneRecharges", headers=headers).status_code == 200
    assert str(recharge) == "284206977373282501394198671064916751422"


@pytest.mark.parametrize("recharge__phone_number", ["5511999553492"])
def test_get_endpoint_recharge_post(client, recharge):
    payload = json.dumps(
        {"product_id": "claro_20", "phone_number": "5511999553492", "value": 20.00}
    )
    client.post("/PhoneRecharges", data=payload)
    assert recharge.phone_number == "5511999553492"


def test_get_endpoint_recharge_post_201(client, recharge):

    payload = json.dumps(
        {
            "product_id": recharge.product_id,
            "phone_number": recharge.phone_number,
            "value": recharge.value,
        }
    )
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }

    assert (
        client.post("/PhoneRecharges", headers=headers, data=payload).status_code == 201
    )


def test_get_recharge(client, recharge):
    assert recharge.phone_number == "5511969999999"
    assert recharge.value == 20.0
    assert recharge.product_id == "claro_20"
    assert recharge.created_at == "2021-10-11T21:23:16.220005"


@pytest.mark.parametrize("recharge__phone_number", ["5511969999999"])
def test_get_endpoint_get_recharge_by_phone_number(client, recharge):
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }
    phone_number = recharge.phone_number
    payload = {}
    assert (
        client.get(
            f"/PhoneRecharges?phone_number={phone_number}",
            headers=headers,
            data=payload,
        ).status_code
        == 200
    )


def test_get_endpoint_get_recharge_by_id_recharge(client, recharge):
    id = session.query(Recharge.public_id).first()
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }

    print(f"id get recharge {id[0]}")

    assert (
        client.get(
            f"/PhoneRecharges?id={id[0]}",
            headers=headers,
        ).status_code
        == 200
    )


def test_get_endpoint_get_recharge_by_id_recharge_not_found(client, recharge):
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }

    assert (
        client.get(
            f"/PhoneRecharges?id=9999999999999",
            headers=headers,
        ).status_code
        == 404
    )


def test_get_endpoint_get_recharge_by_phone_number_not_found(client, recharge):
    headers = {
        "Authorization": "Basic bWFyY29zcGF1bG8uc2lsdmF2aWFuYUBnbWFpbC5jb206bGF5bGFlYmVs"
    }
    payload = {}
    assert (
        client.get(
            "/PhoneRecharges?phone_number=0000000000000", headers=headers, data=payload
        ).status_code
        == 404
    )


def test_get_unauthorized(client, recharge):
    assert (
        client.get(
            "/PhoneRecharges",
        ).status_code
        == 401
    )


def test_get_products_unauthorized(client, product):
    assert (
        client.get(
            "/CompanyProducts",
        ).status_code
        == 401
    )
