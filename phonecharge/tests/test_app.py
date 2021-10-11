import json



def test_get_root_endpoint(client):
    assert client.get("/").status_code == 404


def test_get_endpoint_products(client, product):
    assert client.get("/CompanyProducts")
    
       

def test_get_endpoint_product_id(client, product):
    assert client.get("/CompanyProducts")
   
