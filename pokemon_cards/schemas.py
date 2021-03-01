from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from pokemon_cards.models import Pokemon, User, Deck, CardDeck, Wishlist, WishlistCards, Trades

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


class CardDeck(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CardDeck
        sqla_session = db.session


class Wishlist(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Wishlist
        sqla_session = db.session


class WishlistCards(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WishlistCards
        sqla_session = db.session


class Trades(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trades
        sqla_session = db.session
