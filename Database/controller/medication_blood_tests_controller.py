from flask import Blueprint, jsonify, request

from extensions import db
from models.medications_blood_tests import MedicationBloodTests, MedicationBloodTestsSchema

medication_blood_tests_endpoints = Blueprint('medication_blood_tests_endpoints', __name__)
single_medication_blood_tests_schema = MedicationBloodTestsSchema()
many_medication_blood_tests_schema = MedicationBloodTestsSchema(many=True)


@medication_blood_tests_endpoints.route('/get_medication_blood_test/<string:medication_name>/<string:blood_test_type>', methods=['GET'])
def get_medication_blood_test(medication_name: str, blood_test_type: str) -> (dict, int):
    blood_test = MedicationBloodTests.query.filter_by(medication=medication_name,
                                                      blood_test=blood_test_type
                                                      ).first()
    if blood_test:
        return single_medication_blood_tests_schema.jsonify(blood_test), 200
    else:
        return jsonify(msg='Could not find blood test'), 404


@medication_blood_tests_endpoints.route('/get_medication_blood_tests/<string:medication_name>', methods=['GET'])
def get_medication_blood_test_by_name(medication_name: str) -> (dict, int):
    blood_tests = MedicationBloodTests.query.filter_by(medication=medication_name).all()
    return many_medication_blood_tests_schema.jsonify(blood_tests), 200


@medication_blood_tests_endpoints.route('/add_medication_blood_test', methods=['POST'])
def add_medication_blood_test() -> (dict, int):
    data = request.json if request.is_json else request.form
    medication_blood_test = MedicationBloodTests(
        medication=data['medication_name'],
        blood_test=data['blood_test_type'],
        frequency_days=data['frequency_days'],
        mandatory=data['mandatory']
    )
    db.session.add(medication_blood_test)
    db.session.commit()
    return single_medication_blood_tests_schema.jsonify(medication_blood_test), 201
