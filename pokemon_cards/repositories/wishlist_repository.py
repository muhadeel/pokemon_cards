from typing import Optional, List, Dict, Any, Union
from sqlalchemy.orm import load_only

from pokemon_cards.models import Wishlist, WishlistCards
from pokemon_cards.repositories import BaseRepository


class WishlistRepository(BaseRepository):
    """
    base class for all of the repos

    """

    def __init__(self):
        super().__init__(model=Wishlist)


    def get_by_user_id(self, user_id: int, only: Optional[List[str]] = None) -> Wishlist:
        """
        Get Wishlist of user

        :param user_id:
        :param only:
        :return: wishlist
        """
        query = self.db_session.query(self.model).filter(self.model.user_id == user_id)
        if only:
            query = query.options(load_only(*only))
        return query.one_or_none()

    
    def add_cards_to_wishlist(self, user_id: int, cards_ids: List[str]) -> Wishlist:
        """
        adds card(s) to wishlist

        :param user_id:
        :param cards_ids:
        :return: wishlist
        """
        # query the dataset for the existing wishlist
        query = self.db_session.query(self.model).filter(self.model.user_id == user_id)
        wishlist = query.one_or_none()
        # find existing cards in wishlist and new cards not already in wishlist
        existing_cards_ids = set([card.card_id for card in wishlist.cards])
        new_cards_ids = set(cards_ids).difference(existing_cards_ids)
        # create new card list of exisiting cards and new cards then commit 
        if len(new_cards_ids) > 0:
            create_data_list = [{WishlistCards.card_id.key: card_id, WishlistCards.user_id.key: user_id} for card_id in
                                new_cards_ids]
            self.db_session.bulk_insert_mappings(WishlistCards, create_data_list)
            self.db_session.commit()
        return wishlist

    def remove_cards_from_wishlist(self, user_id: int, cards_ids: List[str]) -> Wishlist:
        """
        remove card(s) from wishlist

        :param user_id:
        :param cards_ids:
        :return: wishlist
        """
        # query the dataset for the existing wishlist
        query = self.db_session.query(self.model).filter(self.model.user_id == user_id)
        wishlist = query.one_or_none()
        # find existing cards in wishlist that intersect with list of cards to remove
        existing_cards_ids = set([card.card_id for card in wishlist.cards])
        cards_ids_to_remove = set(cards_ids).intersection(existing_cards_ids)
        # create new card list with updated card list then commit
        if len(cards_ids_to_remove) > 0:
            for card_id in cards_ids_to_remove:
                query = self.db_session.query(WishlistCards).filter(WishlistCards.user_id == user_id). \
                    filter(WishlistCards.card_id == card_id)
                query.delete(synchronize_session=False)

            self.db_session.commit()
        return wishlist
