from typing import Dict, Any, List

from flask_restful import abort

from pokemon_cards.models import Deck
from pokemon_cards.repositories.deck_repository import DeckRepository
from pokemon_cards.repositories.user_repository import UserRepository


class DeckComponent(object):
    def __init__(self):
        self.repository = DeckRepository()

    def get_all_user_decks(self, user_email: str) -> List[Deck]:
        """
        Get all Decks by user_email

        :param user_email:
        :return:
        """
        user = UserRepository().get_user_id_by_email(user_email=user_email)
        decks = self.repository.get_records_by_user_email(user_id=user.id, only=[Deck.id.key, Deck.description.key])
        return decks

    def get_by_id(self, deck_id: int):
        deck = self.repository.get_by_id(record_id=deck_id)
        return deck

    def create_deck(self, data: Dict[str, Any]) -> Deck:
        """
        Create a new Deck

        :param data:
        :return:
        """
        create_data = self.__prepare_creation_data(data=data)
        deck = self.repository.create_record(create_data=create_data)
        return deck

    def add_cards_to_deck_by_id(self, deck_id: int, cards_ids: List[str]) -> Deck:
        """

        :param deck_id:
        :param cards_ids:
        :return:
        """
        deck = self.repository.add_cards_to_deck(deck_id=deck_id, cards_ids=cards_ids)
        return deck

    def remove_cards_from_deck_by_id(self, deck_id: int, cards_ids: List[str]) -> Deck:
        """

        :param deck_id:
        :param cards_ids:
        :return:
        """
        deck = self.repository.remove_cards_from_deck(deck_id=deck_id, cards_ids=cards_ids)
        return deck

    def update_deck(self, deck_id: int, data: Dict[str, Any]) -> int:
        """
        Update a deck

        :param deck_id:
        :param data:
        :return:
        """
        count = 0
        update_data = self.__prepare_update_data(data=data)
        if update_data:
            self._check_deck_exists(deck_id=deck_id)
            count = self.repository.update_record(record_id=deck_id, update_data=update_data)
        return count

    def delete_deck(self, deck_id: int) -> int:
        """
        Delete a deck

        :param deck_id:
        :return:
        """
        self._check_deck_exists(deck_id=deck_id)
        count = self.repository.delete_record(record_id=deck_id)
        return count

    def _check_deck_exists(self, deck_id: int) -> Deck:
        """
        Check if the deck exists, if not, will return 404

        :param deck_id:
        :return:
        """
        deck = self.get_by_id(deck_id=deck_id)
        if not deck:
            abort(404, message=f"Deck {deck_id} doesn't exist")
        return deck

    def __prepare_creation_data(self, data: Dict) -> Dict:
        create_data = {}

        # TODO change to get and validate user by email after implementing the user logic
        if Deck.user_id.key in data:
            create_data[Deck.user_id.key] = int(data[Deck.user_id.key])
        if Deck.description.key in data:
            create_data[Deck.description.key] = data[Deck.description.key]
        if not create_data:
            raise Exception("Deck creation failed. Missing user_id!")
        return create_data

    def __prepare_update_data(self, data: Dict) -> Dict:
        update_data = {}

        if Deck.user_id.key in data:
            update_data[Deck.user_id.key] = int(data[Deck.user_id.key])
        if Deck.description.key in data:
            update_data[Deck.description.key] = data[Deck.description.key]
        return update_data
