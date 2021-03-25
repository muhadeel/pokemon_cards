from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from pokemon_cards.constants import SuperType

Base = declarative_base()

db = SQLAlchemy()


class BaseModelMixin(object):
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())


class Pokemon(Base, BaseModelMixin):
    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)


class User(Base, BaseModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    email = db.Column(db.String(127), nullable=False, unique=True)
    name = db.Column(db.String(53), nullable=False)
    bio = db.Column(db.String(255))
    # Relationships to other tables
    decks = relationship("Deck", back_populates="user", uselist=True)
    wishlists = relationship("Wishlist", back_populates="user", uselist=True)


class Card(Base, BaseModelMixin):
    __tablename__ = 'cards'
    id = db.Column(db.String(255), primary_key=True, nullable=False)
    name = db.Column(db.String(127), nullable=False)
    supertype = db.Column(db.Enum(*SuperType.SuperTypes), nullable=False)
    subtype = db.Column(db.String(63))


class Deck(Base, BaseModelMixin):
    __tablename__ = 'decks'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    # TODO the ondelete is currently set to SET NULL just in case it breaks anything - please change to CASCADE later.
    user_id = db.Column(db.Integer(), ForeignKey("users.id", ondelete="SET NULL"), nullable=False)
    description = db.Column(db.String(255))
    # Relationships to other tables
    user = relationship("User", back_populates="decks", uselist=False)
    cards = relationship("CardDeck", backref="decks", uselist=True)


class CardDeck(Base, BaseModelMixin):
    __tablename__ = 'card_deck'
    card_id = db.Column(db.String(255), db.ForeignKey("cards.id"), primary_key=True, nullable=False)
    deck_id = db.Column(db.Integer(), db.ForeignKey("decks.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    # Relationships to other tables
    card = relationship("Card", backref="carddeck_card", foreign_keys=[card_id], uselist=False)


class Wishlist(Base, BaseModelMixin):
    __tablename__ = 'wishlists'
    user_id = db.Column(db.Integer(), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    # Relationships to other tables
    user = relationship("User", back_populates="wishlists")
    cards = relationship("WishlistCards", backref="wishlists", uselist=True)


class WishlistCards(Base, BaseModelMixin):
    __tablename__ = 'wishlist_cards'
    user_id = db.Column(db.Integer(), ForeignKey('wishlists.user_id', ondelete="CASCADE"), primary_key=True,
                        nullable=False)
    card_id = db.Column(db.String(255), ForeignKey('cards.id'), primary_key=True, nullable=False)
    threshold = db.Column(db.Float)
    # Relationships to other tables
    user = relationship('User', primaryjoin=user_id == User.id , backref="wishlistcards_user",
                        foreign_keys=[user_id], uselist=False)
    card = relationship('Card', backref="wishlistcards_card", foreign_keys=[card_id], uselist=False)


class Trades(Base, BaseModelMixin):
    __tablename__ = 'trades'
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    seller_id = db.Column(db.Integer(), ForeignKey('users.id'), nullable=False)
    purchaser_id = db.Column(db.Integer(), ForeignKey('users.id'), nullable=False)
    card_id = db.Column(db.String(255), ForeignKey('cards.id'), nullable=False)
    # Relationships to other tables
    seller_user = relationship('User', backref="trades_seller", foreign_keys=[seller_id], uselist=False)
    purchaser_user = relationship('User', backref="trades_purchaser", foreign_keys=[purchaser_id], uselist=False)
    card = relationship('Card', backref="trades_card", foreign_keys=[card_id], uselist=False)
