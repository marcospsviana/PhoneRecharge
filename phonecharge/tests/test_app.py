def test_get_root_endpoint(client, db):
    assert client.get("/").status_code == 400
