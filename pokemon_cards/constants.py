from typing import List

APP_VERSION = 'v1'


class SuperType(object):
    TRAINER: str = "Trainer"
    POKEMON: str = "Pokémon"
    ENERGY: str = "Energy"
    SuperTypes: List = [TRAINER, POKEMON, ENERGY]
