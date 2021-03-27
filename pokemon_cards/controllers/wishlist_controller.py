from flask import request, Blueprint, make_response
from flask_restful import Api, Resource, abort

from pokemon_cards.components.wishlist_components import WishlistComponent
from pokemon_cards.schemas import WishlistSchema

wishlist_bp = Blueprint('wishlist', __name__)
wishlist_api = Api(wishlist_bp)

# controller for the wishlist itself
class WishlistController(Resource):
    def __init__(self):
        self.component = WishlistComponent()
    
    def get(self, user_id):
        wishlist = self.component.get_by_user_id(user_id = user_id)
        if not wishlist:
            abort(404, message=f"wishlist with user id {user_id} doesn't exist")
        
        # convert the wishlist object into json format
        wishlist_schema = WishlistSchema()
        wishlist_json = wishlist_schema.dump(wishlist)
        return make_response({'Wishlist': wishlist_json}, 200)


# controller for the cards inside the wishlst
class WishlistCardController(Resource):
    def __init__(self):
        self.component = WishlistComponent()

    def put(self, user_id):
        count = self.component.update_wishlist(user_id=user_id, data=request.get_json())
        return make_response({'message': 'Success', 'count': count}, 200)

    def post(self, user_id):
        data = request.get_json()
        cards_ids = data.get('cards')
        if not cards_ids:
            abort(422, message=f"Unprocessable Entity, must provide cards list of ids.")

        wishlist = self.component.add_cards_to_wishlist_by_id(user_id=user_id, cards_ids=cards_ids)

        # convert the wishlist object into json format
        wishlist_schema = WishlistSchema(many=False)
        wishlist_json = wishlist_schema.dump(wishlist)
        return make_response({'wishlist': wishlist_json}, 201)

    def delete(self, user_id):
        data = request.get_json()
        cards_ids = data.get('cards')
        if not cards_ids:
            abort(422, message=f"Unprocessable Entity, must provide cards list of ids.")
        wishlist = self.component.remove_cards_from_wishlist_by_id(user_id=user_id, cards_ids=cards_ids)

        # convert the wishlist object into json format
        wishlist_schema = WishlistSchema(many=False)
        wishlist_json = wishlist_schema.dump(wishlist)
        return make_response({'wishlist': wishlist_json}, 200)
        


# add the resource to the api (suffix)
wishlist_api.add_resource(WishlistController, '/<int:user_id>')
wishlist_api.add_resource(WishlistCardController, '/<int:user_id>/cards')