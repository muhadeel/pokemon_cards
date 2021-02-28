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
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id", ondelete="SET NULL"), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    # Relationships to other tables
    user = relationship("User", back_populates="decks")


    # sam's changes (testing git commands)
class Wishlist(db.Model, BaseModelMixin):
    id = db.Column(db.String(255), primary_key=True)
    # TODO the ondelete is currently set to SET NULL just in case it breaks anything - please change to CASCADE later.
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id", ondelete="SET NULL"), nullable=False)
    # Relationships to other tables
    user = relationship("User", back_populates="wishlists")
