import json

def test_create_game_200(test_app, test_db):
    """test the create game POST route"""

    client = test_app.test_client()
    resp = client.post(
        "/api/v1/games",
        content_type="application/json",
        data=json.dumps({
            "name": "EA Cricket 2007",
            "price": 10.99,
            "space": 1610612736
        })
    )

    assert resp.status_code == 201
    assert resp.content_type == "application/json"