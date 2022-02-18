import json

def test_best_value_games_200(test_app, test_db, add_game):
    """test the best value games POST route"""
    
    _game1 = add_game("PUBG", 20.99, 3758096384)
    _game2 = add_game("Free Fire", 15.99, 1073741824)
    _game2 = add_game("COD", 18.99, 2684354560)
    client = test_app.test_client()

    resp = client.post(
        "/api/v1/best_value_games?pen_drive_space=5368709120"
    )

    data = json.loads(resp.data.decode())

    assert resp.status_code == 200
    assert resp.content_type == "application/json"