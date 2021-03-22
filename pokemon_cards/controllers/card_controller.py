from distutils.util import strtobool

from flask import request, Blueprint, make_response
from flask_restful import Api, Resource, abort

from pokemon_cards.components.card_component import CardComponent

cards_bp = Blueprint('cards', __name__)
card_api = Api(cards_bp)


class CardController(Resource):
    def __init__(self):
        self.component = CardComponent()

    def get(self, card_id):
        card = self.component.get_by_id(card_id=card_id)
        if not card:
            abort(404, message=f"Card {card_id} doesn't exist")

        return make_response({'Card': card}, 200)


class CardListController(Resource):
    def __init__(self):
        self.component = CardComponent()

    def get(self):
        current_page = int(request.args.get('current_page', 0))
        if current_page == 0:
            abort(422, message=f"Unprocessable Entity, missing current_page.")
        limit = int(request.args.get('limit', 20))
        short = bool(strtobool(request.args.get('short', "False")))
        cards = self.component.paginate_cards(current_page=current_page,
                                              limit=limit,
                                              short=short)
        return make_response({'Cards': cards}, 200)


card_api.add_resource(CardController, '/<string:card_id>')
card_api.add_resource(CardListController, '')
