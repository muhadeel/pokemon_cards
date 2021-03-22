from typing import List, Optional

from sqlalchemy.orm import load_only

from pokemon_cards.models import Card
from pokemon_cards.repositories import BaseRepository


class CardRepository(BaseRepository):
    """
    base class for all of the repos
    """

    def __init__(self):
        super().__init__(model=Card)

    def get_by_ids(self, cards_ids: List[str], only: Optional[List[str]] = None) -> List[Card]:
        """

        :param cards_ids:
        :param only:
        :return:
        """
        query = self.db_session.query(self.model).filter(self.model.id.in_(cards_ids))
        if only:
            query = query.options(load_only(*only))
        return query.all()
