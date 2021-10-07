def test_get_root_endpoint(client, db):
    assert client.get("/").status_code == 404


def test_get_endpoint_products(client, db):
    assert client.get("/CompanyProducts").status_code == 200
