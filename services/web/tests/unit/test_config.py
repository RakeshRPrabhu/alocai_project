import os

def test_development_config(test_app):
    test_app.config.from_object("project.config.Config")
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_URL")

def test_testing_config(test_app):
    test_app.config.from_object("project.config.TestConfig")
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("TEST_DATABASE_URL")