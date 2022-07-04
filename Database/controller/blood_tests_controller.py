from flask import Blueprint, jsonify, request

from extensions import db
from models.blood_tests import BloodTests, BloodTestsSchema

blood_tests_endpoints = Blueprint('blood_tests_endpoints', __name__)
blood_test_schema = BloodTestsSchema()


@blood_tests_endpoints.route('/get_blood_test/<string:blood_test_type>', methods=['GET'])
def get_blood_test(blood_test_type: str) -> (dict, int):
    blood_test = BloodTests.query.filter_by(blood_test_type=blood_test_type).first()
    if blood_test:
        return blood_test_schema.jsonify(blood_test), 200
    else:
        return jsonify(msg='Could not find blood test'), 404


@blood_tests_endpoints.route('/add_blood_test', methods=['POST'])
def add_blood_test() -> (dict, int):
    data = request.json if request.is_json else request.form
    blood_test = BloodTests(
        blood_test_type=data['blood_test_type'],
        hours_before_results=data['hours_before_results']
    )
    db.session.add(blood_test)
    db.session.commit()
    return blood_test_schema.jsonify(blood_test), 201
