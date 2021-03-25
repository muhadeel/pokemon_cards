from typing import Dict, Any, List

from flask_restful import abort

from pokemon_cards.models import Wishlist
from pokemon_cards.repositories.wishlist_repository import WishlistRepository


class WishlistComponent(object):
    def __init__(self):
        self.repository = WishlistRepository()

    def get_by_user_id(self, user_id: int):
        """

        Get Wishlist by user_id

        :param user_id
        :return: Wishlist
        """
        wishlist = self.repository.get_by_user_id(user_id = user_id)
        return wishlist

    def add_cards_to_wishlist_by_id(self, user_id: int, cards_ids: List[str]) -> Wishlist:
        """
        Add card(s) to Wishlist

        :param user_id:
        :param cards_ids:
        :return:
        """
        wishlist = self.repository.add_cards_to_wishlist(user_id= user_id, cards_ids=cards_ids)
        return wishlist

    def remove_cards_from_wishlist_by_id(self, user_id: int, cards_ids: List[str]) -> Wishlist:
        """
        Remove card(s) from Wishlist

        :param user_id:
        :param cards_ids:
        :return:
        """
        wishlist = self.repository.remove_cards_from_wishlist(user_id=user_id, cards_ids=cards_ids)
        return wishlist

    
