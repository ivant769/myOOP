from flask import request, jsonify, make_response
from flask_restful import Resource
from projectoop.database.db_human import get, delete
from projectoop.database.db_service import receive_all, create, refresh


class Humans(Resource):
    def get(self, id):
        return jsonify(get(id))

    def put(self, id):
        dict_array = request.get_json()
        return jsonify(refresh(dict_array, id))

    def delete(self, id):
        return jsonify(delete(id))


class HumansList(Resource):
    def get(self):
        return make_response(jsonify(receive_all()))

    def post(self):
        return make_response(jsonify(create(request.get_json())))
