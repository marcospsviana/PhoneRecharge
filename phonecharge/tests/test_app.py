import json


def test_get_root_endpoint(client, db):
    assert client.get("/").status_code == 404


def test_get_endpoint_products(client, db):
    assert client.get("/CompanyProducts")
    
       

def test_get_endpoint_product_id(client, db):
    print(f"products {db}")
    assert client.get("/CompanyProducts")
   
