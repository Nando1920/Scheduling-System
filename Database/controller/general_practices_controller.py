from flask import Blueprint, jsonify

from models.general_practices import GeneralPractices, GeneralPracticesSchema

general_practice_endpoints = Blueprint('general_practice_endpoints', __name__)
single_general_practice_schema = GeneralPracticesSchema()


@general_practice_endpoints.route('/get_general_practice/<int:gp_id>', methods=['GET'])
def get_general_practice(gp_id: int) -> (dict, int):
    gp = GeneralPractices.query.filter_by(id=gp_id).first()
    if gp:
        return single_general_practice_schema.jsonify(gp), 200
    else:
        return jsonify(msg='Could not find a GP with that id'), 404
