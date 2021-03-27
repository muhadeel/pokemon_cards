from typing import Dict, Any, List

from flask_restful import abort

from pokemon_cards.models import Deck, User
from pokemon_cards.repositories.deck_repository import DeckRepository
from pokemon_cards.repositories.user_repository import UserRepository


class DeckComponent(object):
    def __init__(self):
        self.repository = DeckRepository()

    def get_decks_by_user(self, user_email: str) -> List[Deck]:
        """
        Get all Decks by user_email

        :param user_email:
        :return:
        """
        # first get the user by email from DB
        user = UserRepository().get_user_by_email(user_email=user_email)
        # then get all decks that belongs to this user from DB
        decks = self.repository.get_records_by_user_email(user_id=user.id, only=[Deck.id.key, Deck.description.key])
        return decks

    def get_by_id(self, deck_id: int):
        """
        Get deck by id

        :param deck_id:
        :return:
        """
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
        email = data.get(User.email.key)
        if not email:
            abort(422, message=f"Unprocessable Entity, deck creation failed. Must provide email!")
        user = UserRepository().get_user_by_email(user_email=email)
        if not user:
            abort(422, message=f"Unprocessable Entity, user with email {email} does not exists!!")
        create_data[Deck.user_id.key] = user.id
        if Deck.description.key in data:
            create_data[Deck.description.key] = data[Deck.description.key]
        return create_data

    def __prepare_update_data(self, data: Dict) -> Dict:
        update_data = {}
        if Deck.description.key in data:
            update_data[Deck.description.key] = data[Deck.description.key]
        return update_data
