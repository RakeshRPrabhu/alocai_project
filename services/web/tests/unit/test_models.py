from project.models import Game

def test_new_game():
    """
    GIVEN a GAME model
    WHEN a new game is created
    THEN check the fields are defined correctly
    """
    game = Game(name= 'Fortnite', price= 71.7, space= 1073741824)
    assert game.name == 'Fortnite'
    assert game.price == 71.7
    assert game.space == 1073741824