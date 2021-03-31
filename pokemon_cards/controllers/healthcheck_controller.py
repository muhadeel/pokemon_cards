from flask import Blueprint, make_response
from flask_restful import Api, Resource

health_check_bp = Blueprint('health_check', __name__)
health_check_api = Api(health_check_bp)


class HealthCheckController(Resource):
    # if app is running then return success
    def get(self):
        return make_response({'Status': 'Success'}, 200)


# add the resource to the api (suffix)
health_check_api.add_resource(HealthCheckController, '')
