from flask_sqlalchemy import SQLAlchemy

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
    id = db.Column(db.Integer(11), primary_key=True)
    email = db.Column(db.String(127), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, )
    bio = db.Column(db.String(255))