import json

def test_db_conn_get_200(test_app):
    """test the db connection GET route"""

    client = test_app.test_client()
    resp = client.get("/api/v1/status")
    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert "healthy" in data["database"]

def test_db_conn_head_200(test_app):
    """test the db connection HEAD route"""

    client = test_app.test_client()
    resp = client.head("/api/v1/status")

    assert resp.status_code == 200