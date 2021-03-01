from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

from pokemon_cards.constants import SuperType

db = SQLAlchemy()


class BaseModelMixin(object):
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now())


class Pokemon(db.Model, BaseModelMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(64), nullable=False)


class Card(db.Model, BaseModelMixin):
    id = db.Column(db.String(255), primary_key=True, nullable=False)
    name = db.Column(db.String(127), nullable=False)
    supertype = db.Column(db.Enum(*SuperType.SuperTypes), nullable=False)
    subtype = db.Column(db.String(63))
    # Relationships to other tables


class User(db.Model, BaseModelMixin):
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    email = db.Column(db.String(127), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, )
    bio = db.Column(db.String(255))
    # Relationships to other tables
    decks = relationship("Deck", back_populates="user", uselist=True)
    wishlists = relationship("Wishlist", back_populates="user", uselist=True)


class Deck(db.Model, BaseModelMixin):
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    # TODO the ondelete is currently set to SET NULL just in case it breaks anything - please change to CASCADE later.
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id", ondelete="SET NULL"), nullable=False)
    description = db.Column(db.String(255))
    # Relationships to other tables
    user = relationship("User", back_populates="decks", uselist=False)


class CardDeck(db.Model, BaseModelMixin):
    card_id = db.Column(db.String(255), db.ForeignKey("card.id"), primary_key=True, nullable=False)
    deck_id = db.Column(db.Integer(), db.ForeignKey("deck.id", ondelete="CASCADE"), primary_key=True, nullable=False)
    # Relationships to other tables
    card = relationship("Card", backref="carddeck_card", foreign_keys=[card_id], uselist=False)
    deck = relationship("Deck", backref="carddeck_deck", foreign_keys=[deck_id], uselist=False)


class Wishlist(db.Model, BaseModelMixin):
    id = db.Column(db.String(255), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    # Relationships to other tables
    user = relationship("User", back_populates="wishlists")


class WishlistCards(db.Model, BaseModelMixin):
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete="CASCADE"), primary_key=True,
                        nullable=False)
    card_id = db.Column(db.String(255), db.ForeignKey('card.id'), primary_key=True, nullable=False)
    threshold = db.Column(db.Float)
    # Relationships to other tables
    user = relationship('User', backref="wishlistcards_user", foreign_keys=[user_id], uselist=False)
    card = relationship('Card', backref="wishlistcards_card", foreign_keys=[card_id], uselist=False)


class Trades(db.Model, BaseModelMixin):
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    seller_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    purchaser_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    card_id = db.Column(db.String(255), db.ForeignKey('card.id'), nullable=False)
    # Relationships to other tables
    seller_user = relationship('User', backref="trades_seller", foreign_keys=[seller_id], uselist=False)
    purchaser_user = relationship('User', backref="trades_purchaser", foreign_keys=[purchaser_id], uselist=False)
    card = relationship('Card', backref="trades_card", foreign_keys=[card_id], uselist=False)
