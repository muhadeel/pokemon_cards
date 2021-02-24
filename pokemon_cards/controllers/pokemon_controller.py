from flask import request, Blueprint, make_response
from flask_restful import Api, Resource, abort

from pokemon_cards.components.pokemon_component import PokemonComponent
from pokemon_cards.schemas import PokemonSchema

pokemons_bp = Blueprint('pokemons', __name__)
pokemon_api = Api(pokemons_bp)


class PokemonController(Resource):
    def __init__(self):
        self.component = PokemonComponent()

    def get(self, pokemon_id):
        pokemon = self.component.get_by_id(pokemon_id=pokemon_id)
        if not pokemon:
            abort(404, message=f"Pokemon {pokemon_id} doesn't exist")

        pokemon_schema = PokemonSchema(many=False)
        pokemon_json = pokemon_schema.dump(pokemon)
        return make_response({'Pokemon': pokemon_json}, 200)

    def delete(self, pokemon_id):
        count = self.component.delete_pokemon(pokemon_id=pokemon_id)
        return make_response({'message': 'Success', 'count': count}, 200)

    def put(self, pokemon_id):
        count = self.component.update_pokemon(pokemon_id=pokemon_id, data=request.get_json())
        return make_response({'message': 'Success', 'count': count}, 200)


class PokemonListController(Resource):
    def __init__(self):
        self.component = PokemonComponent()

    def get(self):
        pokemons = self.component.get_all()
        pokemon_schema = PokemonSchema(many=True)
        pokemons_json = pokemon_schema.dump(pokemons)
        return make_response({'Pokemons': pokemons_json}, 200)

    def post(self):
        pokemon = self.component.create_pokemon(data=request.get_json())
        pokemon_schema = PokemonSchema(many=False)
        pokemon_json = pokemon_schema.dump(pokemon)
        return make_response({'Pokemon': pokemon_json}, 200)


pokemon_api.add_resource(PokemonController, '/<int:pokemon_id>')
pokemon_api.add_resource(PokemonListController, '')
