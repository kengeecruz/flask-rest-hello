"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters, Favorites_Characters
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def all_user():
    users = User.query.all()
    data=[user.serialize() for user in users]
    return jsonify(data), 200

@app.route('/planets', methods=['GET'])
def all_planets():
    planet = Planets.query.all()
    data=[planets.serialize() for planets in planet]
    return jsonify(data)

@app.route('/people', methods=['GET'])
def all_people():
    peoples = Characters.query.all()
    data = [people.serialize()for people in peoples]
    return jsonify(data), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet= Planets.query.filter_by(id=planet_id).first()
    if planet: 
        return jsonify(planet.serialize())
    return jsonify({"No existe planeta"}),400

@app.route('/people/<int:people_id>', methods=['GET'])
def get_pleople(people_id):
    people= Characters.query.filter_by(id=people_id).first()
    if people: 
        return jsonify(people.serialize())

    return jsonify({"No existe "}),400

@app.route('/users/favorites', methods=['GET'])
def favorites():

    return jsonify(response_body), 200





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
1