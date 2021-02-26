from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from pokemon_cards.models import Pokemon

db = SQLAlchemy()
ma = Marshmallow()


class PokemonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pokemon
        sqla_session = db.session
