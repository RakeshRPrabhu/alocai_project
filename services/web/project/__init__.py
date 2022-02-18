from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin

db = SQLAlchemy()

def create_app(): 
    app = Flask(__name__, template_folder= './templates')
    app.config.from_object("project.config.Config")

    db.init_app(app)

    from .views import games_bp
    app.register_blueprint(games_bp)

    spec = APISpec(
        title= "Alocai API Doc",
        version= "1.0.0",
        openapi_version= "3.0.2",
        plugins= [FlaskPlugin(), MarshmallowPlugin()]
    )

    @app.route('/api/swagger.json')
    def create_swagger_spec():
        return jsonify(spec.to_dict())

    with app.test_request_context():
        spec.path(view= views.test_db_connection)
        spec.path(view= views.create_game)
        spec.path(view= views.best_value_games)
    
    return app
