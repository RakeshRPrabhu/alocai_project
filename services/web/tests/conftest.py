import pytest

from project import create_app, db
from project.models import Game


@pytest.fixture(scope="module")
def test_app():
    """
    fixture for testing the application
    """
    app = create_app()
    app.config.from_object("project.config.TestConfig")
    with app.app_context():
        yield app

@pytest.fixture(scope="module")
def test_db():
    """
    fixture for cleaning and leveraging test db
    """
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope="module")
def add_game():
    def _add_game(name, price, space):
        game = Game(name= name, price= price, space= space)
        db.session.add(game)
        db.session.commit()
        return game
    
    return _add_game