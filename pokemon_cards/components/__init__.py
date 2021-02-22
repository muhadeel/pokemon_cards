from pokemon_cards.repositories import BaseRepository


class BaseComponent(object):
    def __init__(self, repository: BaseRepository):
        """

        :param repository: an instance of the corresponding repository to this component
        :type repository:
        """
        self.repository = repository
