
def test_docs_get_200(test_app):
    """test the docs GET route"""

    client = test_app.test_client()
    resp = client.get("/docs")
    assert resp.status_code == 200