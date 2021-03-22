from flask import Blueprint
from pokemontcgsdk import Card as Card_API

from pokemon_cards.components.card_component import CardComponent
from pokemon_cards.models import Card

card_seed = Blueprint('seed_cards', __name__, cli_group=None)


@card_seed.cli.command('seed_cards')
def seed_cards():
    cards = Card_API.all()
    cards_list = [{
        Card.id.key: card.id,
        Card.name.key: card.name,
        Card.subtype.key: card.subtype,
        Card.supertype.key: card.supertype,
    } for card in cards]
    CardComponent().bulk_create_cards(create_data_list=cards_list)


@card_seed.cli.command('test_cards')
def test_cards():
    cards = Card_API.where(supertype='trainer')
    pass
