from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from marshmallow.fields import Nested

from pokemon_cards.models import Pokemon, User, Card, CardDeck, Deck, Wishlist, WishlistCards, Trades

db = SQLAlchemy()
ma = Marshmallow()


class PokemonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemon
        sqla_session = db.session


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        sqla_session = db.session


class CardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Card
        sqla_session = db.session


class CardDeckSchema(ma.SQLAlchemyAutoSchema):
    card = Nested(CardSchema)

    class Meta:
        model = CardDeck
        sqla_session = db.session


class DeckSchema(ma.SQLAlchemyAutoSchema):
    cards = Nested(CardDeckSchema, many=True, exclude=[CardDeck.updated_at.key, CardDeck.created_at.key])

    class Meta:
        model = Deck
        sqla_session = db.session

class WishlistCardsSchema(ma.SQLAlchemyAutoSchema):
    card = Nested(CardSchema)
    
    class Meta:
        model = WishlistCards
        sqla_session = db.session

class WishlistSchema(ma.SQLAlchemyAutoSchema):
    cards = Nested(WishlistCardsSchema, many=True, exclude=[WishlistCards.updated_at.key, WishlistCards.created_at.key])
    class Meta:
        model = Wishlist
        sqla_session = db.session

class TradesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trades
        sqla_session = db.session
