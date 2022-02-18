from flask import Blueprint, jsonify, request, render_template, send_from_directory
from marshmallow import ValidationError
from .models import Game, GameSchema
from project import db
import itertools

# Init Schema
game_schema = GameSchema()
games_schema = GameSchema(many= True)

games_bp = Blueprint('games', __name__)

# Endpoint for checking Database connection
@games_bp.route('/api/v1/status', methods= ['GET', 'HEAD'])
def test_db_connection():
    
    """ Check Database Connection
        ---
        get:
            summary: Check Database Connection
            description: Check Database connection is healthy or unhealthy
            responses:
                200:
                    description: Returns database connection is healthy
                    content:
                        application/json: {}
                500:
                    description: Returns database connection is unhealthy
                    content:
                        application/json: {}
        head:
            summary: Check Database Connection
            description: Check Database connection is healthy or unhealthy
            responses:
                200:
                    description: Returns 200 status code when database connection is healthy
                500:
                    description: Returns 500 status code when database connection is unhealthy
    """

    try:
        db.session.execute('SELECT 1')
        return jsonify(database="healthy"), 200
    except:
        return jsonify(database="unhealthy"), 500


# Endpoint for submitting a game
@games_bp.route('/api/v1/games', methods = ['POST'])
def create_game():

    """ Submit A Game
        ---
        post:
            summary: Submit a game
            requestBody:
                description: "Game Object contain name, price and space parameters" 
                required: true
                content:
                    application/json:
                        schema:
                            type: object
                            required:
                            - name
                            - price
                            - space
                            properties:
                                name:
                                    type: string
                                price:
                                    type: number
                                    format: float
                                space:
                                    type: number
                                    format: int64    

            responses:
                201:
                    description: Returns success response
                    content:
                        application/json:
                            schema: GameSchema
                400:
                    description: Returns error 
                    content:
                        application/json: {}
    """

    data = request.get_json()

    if data is None:
        return jsonify(error= "data is missing!"), 400

    name = data.get('name')
    price = data.get('price')
    space = data.get('space')

    game = Game(name= name, price= price, space= space)

    try:
        game_data = game_schema.load(data)
        db.session.add(game)
        db.session.commit()
        return game_schema.dump(game_data), 201
    
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    except Exception as e:
        return jsonify(name="Name is already taken!"), 400


# Endpoint to check for best value games 
@games_bp.route('/api/v1/best_value_games', methods=['POST'])
def best_value_games():
    
    """ Returns a combination of games
        ---
        post:
            summary: Return a combination of games
            parameters: 
              - in: query
                name: pen_drive_space
                schema:
                    type: integer
                    format: int64
                required: true
                description: Space of Pendrive

            responses:
                200:
                    description: Returns list of games if any
                    content:
                        application/json:
                            schema: GameSchema
                400:
                    description: Returns error 
                    content:
                        application/json: {}   

    """

    pen_drive_space = request.args.get('pen_drive_space', type= int)
    
    if pen_drive_space is None or pen_drive_space <= 0:
        return jsonify(error="Please enter a valid pen drive space"), 400

    game_spaces = Game.query.all()

    a = []
    price_list = []
    space_list = []
    games = None
    for i in range(1, len(game_spaces) + 1):
        for b in itertools.combinations(game_spaces, i):
            a.append(b)
            price=0
            space= 0
            for game in b:
                price += game.price
                space += game.space

            price_list.append(price)
            space_list.append(space)

    sorted_price_list = sorted(range(len(price_list)), key=lambda k: price_list[k], reverse= True)
    for p in sorted_price_list:
        if space_list[p] <= pen_drive_space:
            games = a[p]
            total_space = space_list[p]
            total_price = price_list[p]
            break

    if games == None:
        return jsonify(error="No games are available that fits in the specified pen drive") , 400

    return {
        "games" : games_schema.dump(games),
        "total_space": total_space,
        "remaining_space": pen_drive_space - total_space,
        "total_value": total_price
    }

@games_bp.route('/docs')
@games_bp.route('/docs/<path:path>')
def swagger_docs(path=None):
    if not path or path == 'index.html':
        return render_template('index.html', base_url='/docs')
    else:
        return send_from_directory('./static', path)