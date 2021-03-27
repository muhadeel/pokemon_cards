from distutils.util import strtobool

from flask import request, Blueprint, make_response
from flask_restful import Api, Resource, abort

from pokemon_cards.components.card_component import CardComponent
from pokemon_cards.constants import SuperType

cards_bp = Blueprint('cards', __name__)
card_api = Api(cards_bp)


class CardController(Resource):
    def __init__(self):
        self.component = CardComponent()

    # Get a card by ud
    def get(self, card_id):
        card = self.component.get_by_id(card_id=card_id)
        if not card:
            abort(404, message=f"Card {card_id} doesn't exist")

        return make_response({'Card': card}, 200)


class CardListController(Resource):
    def __init__(self):
        self.component = CardComponent()

    # Get Pokemon cards
    def get(self):
        current_page = int(request.args.get('current_page')) if request.args.get('current_page') else None
        if current_page is None:
            abort(422, message=f"Unprocessable Entity, missing current_page.")
        limit = int(request.args.get('limit', 20))
        if limit not in [10, 20, 25, 50]:
            abort(422, message=f"Unprocessable Entity, we can only view 10, 20, 25, 50 cards per page.")
        short = bool(strtobool(request.args.get('short', "False")))
        # build filters
        filters = dict()
        if request.args.get('name'):
            filters['name'] = request.args.get('name')
        if request.args.get('supertype'):
            if request.args.get('supertype') not in SuperType.SuperTypes:
                abort(422, message=f"Unprocessable Entity, supertype should be {SuperType.SuperTypes}.")
            filters['supertype'] = request.args.get('supertype')
        if request.args.get('set'):
            filters['set'] = request.args.get('set')

        cards = self.component.get_paginated_cards(current_page=current_page,
                                                   limit=limit,
                                                   short=short,
                                                   filters=filters)
        return make_response({'Total': len(cards), 'next_page': current_page+1, 'Cards': cards}, 200)


card_api.add_resource(CardController, '/<string:card_id>')
card_api.add_resource(CardListController, '')
