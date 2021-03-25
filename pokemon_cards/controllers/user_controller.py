from flask import request, Blueprint, make_response
from flask_restful import Api, Resource, abort

from pokemon_cards.components.user_component import UserComponent
from pokemon_cards.schemas import UserSchema

users_bp = Blueprint('users', __name__)
user_api = Api(users_bp)


class UserController(Resource):
    def __init__(self):
        self.component = UserComponent()

    def get(self, user_id):
        user = self.component.get_by_id(user_id=user_id)
        if not user:
            abort(404, message=f"user {user_id} doesn't exist")

        user_schema = UserSchema(many=False)
        user_json = user_schema.dump(user)
        return make_response({'user': user_json}, 200)

    def delete(self, user_id):
        count = self.component.delete_user(user_id=user_id)
        return make_response({'message': 'Success', 'count': count}, 200)

    def put(self, user_id):
        count = self.component.update_user(user_id=user_id, data=request.get_json())
        return make_response({'message': 'Success', 'count': count}, 200)


class UserListController(Resource):
    def __init__(self):
        self.component = UserComponent()

    # GEt all users
    def get(self):
        users = self.component.get_all()
        user_schema = UserSchema(many=True)
        users_json = user_schema.dump(users)
        return make_response({'users': users_json}, 200)

    # CREATE A new user
    def post(self):
        user = self.component.create_user(data=request.get_json())
        user_schema = UserSchema(many=False)
        user_json = user_schema.dump(user)
        return make_response({'user': user_json}, 200)

user_api.add_resource(UserController, '/<int:user_id>')
user_api.add_resource(UserListController, '') 
