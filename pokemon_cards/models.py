from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from pokemon_cards.constants import SuperType

db = SQLAlchemy()


class BaseModelMixin(object):
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())


class Pokemon(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)


class Card(db.Model, BaseModelMixin):
    id = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    supertype = db.Column(db.Enum(*SuperType.SuperTypes), nullable=False)
    subtype = db.Column(db.String(63))


class User(db.Model, BaseModelMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(127), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, )
    bio = db.Column(db.String(255))
    # Relationships to other tables
    decks = relationship("Deck", back_populates="user", uselist=True)
    wishlists = relationship("Wishlist", back_populates="user", uselist=True)


class Deck(db.Model, BaseModelMixin):
    id = db.Column(db.Integer(), primary_key=True)
    # TODO the ondelete is currently set to SET NULL just in case it breaks anything - please change to CASCADE later.
    user_id = db.Column(db.Integer(), db.ForeignKey(
        "user.id", ondelete="SET NULL"), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    # Relationships to other tables
    user = relationship("User", back_populates="decks")


class Wishlist(db.Model, BaseModelMixin):
    id = db.Column(db.String(255), primary_key=True)
    # TODO the ondelete is currently set to SET NULL just in case it breaks anything - please change to CASCADE later.
    user_id = db.Column(db.Integer(), db.ForeignKey(
        "user.id", ondelete="SET NULL"), nullable=False)
    # Relationships to other tables
    user = relationship("User", back_populates="wishlists")


class Wishlist_cards(db.model, BaseModelMixin):
    user_id = db.Column(db.Integer(), primary_key=True)
    ForeignKey('Wishlist.user_id', ondelete="CASCADE")
    card_id = db.Column(db.String(255), primary_key=True)
    ForeignKey('Card.id', ondelete="NO ACTION")
    threshold = db.Column(db.Float)
    user = relationship('Wishlist', back_populates="Wishlist_cards")
    Wishlist_cards = relationship('')


class Trades(db.model, BaseModelMixin):
    id = db.Column(db.Integer(), primary_key=True),
    seller_id = db.Column(db.Integer(), primary_key=False)
    ForeignKey('user.seller_id', ondelete="NO ACTION")
    purchaser_id = db.Column(db.Integer(), primary_key=False)
    ForeignKey('user.purchaser_id', ondelete="NO ACTION")
    card_id = db.Column(db.String(255), primary_key=False)
    ForeignKey('cards.card_id', ondelete="NO ACTION")
    user = relationship('User', back_populates="Trades")
    Trades = relationship('Trades', back_populates="Cards")
