from flask.cli import FlaskGroup
from project import create_app, db

app = create_app()
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    """Method to create the tables"""

    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()