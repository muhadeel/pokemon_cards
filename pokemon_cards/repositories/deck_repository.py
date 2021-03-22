from typing import Optional, List

from sqlalchemy.orm import load_only

from pokemon_cards.models import Deck, CardDeck
from pokemon_cards.repositories import BaseRepository


class DeckRepository(BaseRepository):
    """
    base class for all of the repos
    """

    def __init__(self):
        super().__init__(model=Deck)

    def get_records_by_user_email(self, user_id: int, only: Optional[List[str]] = None):
        """
        Get all records of this model from database

        :param user_id:
        :param only:
        :return:
        """
        query = self.db_session.query(self.model).filter(Deck.user_id == user_id)
        if only:
            query = query.options(load_only(*only))
        return query.all()

    def add_cards_to_deck(self, deck_id: int, cards_ids: List[str]) -> Deck:
        """

        :param deck_id:
        :param cards_ids:
        :return:
        """
        query = self.db_session.query(self.model).filter(self.model.id == deck_id)
        deck = query.one_or_none()
        existing_cards_ids = set([card.card_id for card in deck.cards])
        new_cards_ids = set(cards_ids).difference(existing_cards_ids)
        if len(new_cards_ids) > 0:
            create_data_list = [{CardDeck.card_id.key: card_id, CardDeck.deck_id.key: deck_id} for card_id in
                                new_cards_ids]
            self.db_session.bulk_insert_mappings(CardDeck, create_data_list)
            self.db_session.commit()
        return deck

    def remove_cards_from_deck(self, deck_id: int, cards_ids: List[str]) -> Deck:
        """

        :param deck_id:
        :param cards_ids:
        :return:
        """
        query = self.db_session.query(self.model).filter(self.model.id == deck_id)
        deck = query.one_or_none()
        existing_cards_ids = set([card.card_id for card in deck.cards])
        cards_ids_to_remove = set(cards_ids).intersection(existing_cards_ids)
        if len(cards_ids_to_remove) > 0:
            for card_id in cards_ids_to_remove:
                query = self.db_session.query(CardDeck).filter(CardDeck.deck_id == deck_id). \
                    filter(CardDeck.card_id == card_id)
                query.delete(synchronize_session=False)

            self.db_session.commit()
        return deck
