from typing import Dict, Any, List

from flask_restful import abort
from pokemontcgsdk import Card as CardAPI

from pokemon_cards.models import Card
from pokemon_cards.repositories.card_repository import CardRepository


class CardComponent(object):
    def __init__(self):
        self.repository = CardRepository()

    def paginate_cards(self, current_page: int, limit: int = 20, short: bool = False):
        """
        Get cards form Pokemon TCG API, that are with supertype 'pokemon', paginated.
        :param current_page:
        :param limit:
        :param short:
        :return:
        """
        if limit % 5 != 0:
            limit = 20
        sub_size = 100 / limit
        page = int(current_page // sub_size + 1)
        section = int(current_page % sub_size - 1)
        start = section * limit
        end = (section + 1) * limit
        cards = CardAPI.where(page=page, supertype='pokemon')
        cards_list = []
        for card in cards[start:end]:
            cards_list.append(self._transform_card(card=card, short=short))
        return cards_list

    def get_by_id(self, card_id: str):
        card = CardAPI.where(id=card_id).pop()
        return self._transform_card(card=card)

    def bulk_create_cards(self, create_data_list: List[Dict[str, Any]]) -> Card:
        """
        Create bulk cards (atomic transaction)

        :param create_data_list:
        :return:
        """
        card = self.repository.bulk_create_records(create_data_list=create_data_list, commit=True)
        return card

    def update_card(self, card_id: str, data: Dict[str, Any]) -> int:
        """
        Update a card

        :param card_id:
        :param data:
        :return:
        """
        count = 0
        if data:
            self._check_card_exists(card_id=card_id)
            count = self.repository.update_record(record_id=card_id, update_data=data)
        return count

    def _check_card_exists(self, card_id: str) -> Card:
        """
        Check if the card exists, if not, will return 404

        :param card_id:
        :return:
        """
        card = self.get_by_id(card_id=card_id)
        if not card:
            abort(404, message=f"Card {card_id} doesn't exist")
        return card

    def _transform_card(self, card, short: bool = False) -> Dict[str, Any]:
        """
        Takes a list of cards object
        :param card:
        :return:
        """
        if short:
            json_card = {
                'id': card.id,
                'name': card.name,
                'rarity': card.rarity,
                'subtype': card.subtype,
                'supertype': card.supertype,
                'evolves_from': card.evolves_from,
            }
        else:
            json_card = {
                'ability': card.ability,
                'ancient_trait': card.ancient_trait,
                'attacks': card.attacks,
                'evolves_from': card.evolves_from,
                'hp': card.hp,
                'id': card.id,
                'name': card.name,
                'rarity': card.rarity,
                'series': card.series,
                'set': card.set,
                'set_code': card.set_code,
                'subtype': card.subtype,
                'supertype': card.supertype,
                'text': card.text,
                'types': card.types,
                'weaknesses': card.weaknesses,
            }
        return json_card
