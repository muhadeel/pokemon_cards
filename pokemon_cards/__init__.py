from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from pokemon_cards.commads.cards_seed import card_seed
from pokemon_cards.constants import APP_VERSION
from pokemon_cards.controllers.card_controller import cards_bp
from pokemon_cards.controllers.deck_controller import decks_bp
from pokemon_cards.controllers.healthcheck_controller import health_check_bp
from pokemon_cards.controllers.user_controller import users_bp
from pokemon_cards.controllers.wishlist_controller import wishlist_bp
from pokemon_cards.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy()
ma = Marshmallow()
db.init_app(app)

# register here all your routes
app.register_blueprint(cards_bp, url_prefix=f'/{APP_VERSION}/cards')
app.register_blueprint(decks_bp, url_prefix=f'/{APP_VERSION}/decks')
app.register_blueprint(wishlist_bp, url_prefix=f'/{APP_VERSION}/wishlist')
app.register_blueprint(users_bp, url_prefix=f'/{APP_VERSION}/users')
app.register_blueprint(health_check_bp, url_prefix=f'/{APP_VERSION}/health_check')

# register commands
app.register_blueprint(card_seed)
