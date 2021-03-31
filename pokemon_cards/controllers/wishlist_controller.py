from flask import request, Blueprint, make_response
from flask_restful import Api, Resource, abort

from pokemon_cards.components.wishlist_components import WishlistComponent
from pokemon_cards.schemas import WishlistSchema

wishlist_bp = Blueprint('wishlist', __name__)
wishlist_api = Api(wishlist_bp)

class WishlistController(Resource):
    def __init__(self):
        self.component = WishlistComponent()
    
    # get wishlist by user_id
    def get(self, user_id):
        wishlist = self.component.get_by_user_id(user_id = user_id)
        if not wishlist:
            abort(404, message=f"wishlist with user id {user_id} doesn't exist")
        
        # convert the wishlist object into json format
        wishlist_schema = WishlistSchema()
        wishlist_json = wishlist_schema.dump(wishlist)
        return make_response({'Wishlist': wishlist_json}, 200)


# controller for the cards inside the wishlist
class WishlistCardController(Resource):
    def __init__(self):
        self.component = WishlistComponent()

    # adds cards to the wishlist associated with the user_id
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

    # deletes cards from wishlist associated with the user_id
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
        
class WishlistStatisticsController(Resource):
    def __init__(self):
        self.component = WishlistComponent()

    # get wishlist statistics (count of each supertype [pokemon, trainer, energy])
    def get(self, user_id):
        wishlist = self.component.get_by_user_id(user_id=user_id)
        if not wishlist:
            abort(404, message=f"wishlist with user id {user_id} doesn't exist")
        
        wishlist_schema = WishlistSchema()
        wishlist_json = wishlist_schema.dump(wishlist)

        # finding the count of supertypes in a wishlist
        stats = {"Pokemon cards count": 0, "Trainer cards count": 0, "Energy cards count": 0}
        for card in wishlist_json["cards"]:
            supertype = card['card']['supertype']
            if supertype == "Pokémon":
                stats["Pokemon cards count"] +=1
            elif supertype == "Trainer":   
                stats["Trainer cards count"] +=1
            elif supertype == "Energy": 
                stats["Energy cards count"] +=1
            
        return make_response({"Wishlist Statistics": stats}, 200)

# add the resource to the api (suffix)
wishlist_api.add_resource(WishlistController, '/<int:user_id>')
wishlist_api.add_resource(WishlistCardController, '/<int:user_id>/cards')
wishlist_api.add_resource(WishlistStatisticsController, '/<int:user_id>/cards/stats')