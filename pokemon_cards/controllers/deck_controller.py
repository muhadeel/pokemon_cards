from flask import request, Blueprint, make_response
from flask_restful import Api, Resource, abort

from pokemon_cards.components.deck_component import DeckComponent
from pokemon_cards.schemas import DeckSchema

decks_bp = Blueprint('decks', __name__)
deck_api = Api(decks_bp)


class DeckController(Resource):
    def __init__(self):
        self.component = DeckComponent()

    # Get a deck by deck_id
    def get(self, deck_id):
        deck = self.component.get_by_id(deck_id=deck_id)
        if not deck:
            abort(404, message=f"Deck {deck_id} doesn't exist")

        deck_schema = DeckSchema(many=False)
        deck_json = deck_schema.dump(deck)
        return make_response({'Deck': deck_json}, 200)

    # Delete a deck by deck_id
    def delete(self, deck_id):
        count = self.component.delete_deck(deck_id=deck_id)
        return make_response({'message': 'Success', 'count': count}, 200)

    # Update a deck by deck_id
    def put(self, deck_id):
        count = self.component.update_deck(deck_id=deck_id, data=request.get_json())
        return make_response({'message': 'Success', 'count': count}, 200)


class DeckListController(Resource):
    def __init__(self):
        self.component = DeckComponent()

    # Get all deck that belongs to a specific user
    def get(self):
        user_email = request.args.get('email')
        if not user_email:
            abort(422, message=f"Unprocessable Entity, must provide email.")
        decks = self.component.get_decks_by_user(user_email=user_email)
        deck_schema = DeckSchema(many=True)
        decks_json = deck_schema.dump(decks)
        return make_response({'Decks': decks_json}, 200)

    # Create a new deck for a user
    def post(self):
        deck = self.component.create_deck(data=request.get_json())
        deck_schema = DeckSchema(many=False)
        deck_json = deck_schema.dump(deck)
        return make_response({'Deck': deck_json}, 201)

# controller for the cards inside the deck
class DeckCardController(Resource):
    def __init__(self):
        self.component = DeckComponent()

    # adds cards to a specific deck
    def post(self, deck_id):
        data = request.get_json()
        cards_ids = data.get('cards')
        if not cards_ids:
            abort(422, message=f"Unprocessable Entity, must provide cards list of ids.")

        deck = self.component.add_cards_to_deck_by_id(deck_id=deck_id, cards_ids=cards_ids)

        deck_schema = DeckSchema(many=False)
        deck_json = deck_schema.dump(deck)
        return make_response({'deck': deck_json}, 201)

    # deletes cards from a specific deck
    def delete(self, deck_id):
        data = request.get_json()
        cards_ids = data.get('cards')
        if not cards_ids:
            abort(422, message=f"Unprocessable Entity, must provide cards list of ids.")
        deck = self.component.remove_cards_from_deck_by_id(deck_id=deck_id, cards_ids=cards_ids)

        deck_schema = DeckSchema(many=False)
        deck_json = deck_schema.dump(deck)
        return make_response({'deck': deck_json}, 200)

class DeckStatisticsController(Resource):
    def __init__(self):
        self.component = DeckComponent()

    # get deck statistics (count of each supertype [pokemon, trainer, energy])
    def get(self, deck_id): 
        deck = self.component.get_by_id(deck_id=deck_id)
        if not deck:
            abort(404, message=f"Deck {deck_id} doesn't exist")

        deck_schema = DeckSchema(many=False)
        deck_json = deck_schema.dump(deck)

        # finding the count of supertypes in a deck
        stats = {"Pokemon cards count": 0, "Trainer cards count": 0, "Energy cards count": 0}
        for card in deck_json["cards"]:
            supertype = card['card']['supertype']
            if supertype == "Pokémon":
                stats["Pokemon cards count"] +=1
            elif supertype == "Trainer":   
                stats["Trainer cards count"] +=1
            elif supertype == "Energy": 
                stats["Energy cards count"] +=1
            
        return make_response({"Deck Statistics": stats}, 200)

# add the resource to the api (suffix)
deck_api.add_resource(DeckListController, '')
deck_api.add_resource(DeckController, '/<int:deck_id>')
deck_api.add_resource(DeckCardController, '/<int:deck_id>/cards')
deck_api.add_resource(DeckStatisticsController, '/<int:deck_id>/cards/stats')
