from typing import Dict, Any, List

from flask import render_template

from pokemon_cards.components import BaseComponent
from pokemon_cards.models import Pokemon
from pokemon_cards.repositories.pokemon_repository import PokemonRepository


class PokemonComponent(BaseComponent):
    def __init__(self):
        super().__init__(repository=PokemonRepository())

    def get_all(self) -> List[Pokemon]:
        """
        Get all Pokemons

        :return:
        """
        pokemons = self.repository.get_records()
        return pokemons

    def get_by_id(self, pokemon_id: int):
        pokemon = self.repository.get_by_id(record_id=pokemon_id)
        return pokemon


    def create_pokemon(self, data: Dict[str, Any]) -> Pokemon:
        """
        Create a new Pokemon

        :param data:
        :return:
        """
        create_data = self.__prepare_creation_data(data=data)
        pokemon = self.repository.create_record(create_data=create_data)
        return pokemon

    def update_pokemon(self, pokemon_id: int, data: Dict[str, Any]) -> int:
        """
        Update a pokemon

        :param pokemon_id:
        :param data:
        :return:
        """
        count = 0
        update_data = self.__prepare_update_data(data=data)
        if update_data:
            self.check_pokemon_exist(pokemon_id=pokemon_id)
            count = self.repository.update_record(record_id=pokemon_id, update_data=update_data)
        return count

    def delete_pokemon(self, pokemon_id: int) -> int:
        """
        Delete a pokemon

        :param pokemon_id:
        :return:
        """
        self.check_pokemon_exist(pokemon_id=pokemon_id)
        count = self.repository.delete_record(record_id=pokemon_id)
        return count

    def check_pokemon_exist(self, pokemon_id: int):
        """
        Checks if a pokemon exists if not redirect to resource not found page

        :param pokemon_id:
        :return:
        """
        pokemon = self.get_by_id(pokemon_id=pokemon_id)
        if not pokemon:
            raise Exception(f"Resource not found. id: {pokemon_id}")

    def __prepare_creation_data(self, data: Dict) -> Dict:
        create_data = {}
        if Pokemon.name.key in data:
            create_data[Pokemon.name.key] = data[Pokemon.name.key]

        if not create_data:
            raise Exception("Creation failed. Missing data!")
        return create_data

    def __prepare_update_data(self, data: Dict) -> Dict:
        update_data = {}
        if Pokemon.name.key in data:
            update_data[Pokemon.name.key] = data[Pokemon.name.key]

        return update_data
