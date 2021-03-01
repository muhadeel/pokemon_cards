from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from pokemon_cards.models import Pokemon, User, Deck, Wishlist, Wishlist_cards, Trades

db = SQLAlchemy()
ma = Marshmallow()


class PokemonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemon
        sqla_session = db.session


class User(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session


class Deck(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Deck
        sqla_session = db.session


class Wishlist(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wishlist
        sqla_session = db.session


class Wishlist_cards(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wishlist_cards
        sqla_session = db.session


class Trades(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Trades
        sqla_session = db.session
