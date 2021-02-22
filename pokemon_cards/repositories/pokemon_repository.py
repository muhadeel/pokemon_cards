from app.models import Pokemon
from app.repositories import BaseRepository


class PokemonRepository(BaseRepository):
    """
    base class for all of the repos
    """

    def __init__(self):
        super().__init__(model=Pokemon)
