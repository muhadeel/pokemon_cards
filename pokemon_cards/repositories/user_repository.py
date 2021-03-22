from typing import Optional, List

from sqlalchemy.orm import load_only

from pokemon_cards.models import User
from pokemon_cards.repositories import BaseRepository


class UserRepository(BaseRepository):
    """
    base class for all of the repos
    """

    def __init__(self):
        super().__init__(model=User)

    def get_user_id_by_email(self, user_email: str, only: Optional[List[str]] = None) -> User:
        """
        Get all records of this model from database

        :param user_email:
        :param only:
        :return:
        """
        query = self.db_session.query(self.model).filter(User.email == user_email)
        if only:
            query = query.options(load_only(*only))
        return query.one_or_none()
