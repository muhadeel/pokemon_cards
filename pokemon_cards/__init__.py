from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.controllers.pokemon_controller import pokemons_bp
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
db.init_app(app)

# app.register_blueprint(pokemon_api.blueprint, url_prefix='/pokemons')
app.register_blueprint(pokemons_bp, url_prefix='/pokemons')

from app import routes, models
