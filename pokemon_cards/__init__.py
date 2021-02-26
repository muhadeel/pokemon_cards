from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from pokemon_cards.controllers.pokemon_controller import pokemons_bp
from pokemon_cards.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
ma = Marshmallow()
db.init_app(app)

# register here all your routes
app.register_blueprint(pokemons_bp, url_prefix='/pokemons')

from pokemon_cards import routes, models
