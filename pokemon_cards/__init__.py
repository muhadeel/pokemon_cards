from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from pokemon_cards.commads.cards_seed import card_seed
from pokemon_cards.controllers.card_controller import cards_bp
from pokemon_cards.controllers.deck_controller import decks_bp
from pokemon_cards.controllers.pokemon_controller import pokemons_bp
from pokemon_cards.controllers.wishlist_controller import wishlist_bp
from pokemon_cards.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
ma = Marshmallow()
db.init_app(app)

# register here all your routes
app.register_blueprint(pokemons_bp, url_prefix='/pokemons')
app.register_blueprint(cards_bp, url_prefix='/cards')
app.register_blueprint(decks_bp, url_prefix='/decks')
app.register_blueprint(wishlist_bp, url_prefix='/wishlist')

# register commands
app.register_blueprint(card_seed)

from pokemon_cards import routes, models
