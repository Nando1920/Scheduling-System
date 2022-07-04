from datetime import datetime

from flask import Blueprint, request

from extensions import db
from models.patient_blood_tests import PatientBloodTests, PatientBloodTestsSchema

patient_blood_tests_endpoints = Blueprint('patient_blood_tests_endpoints', __name__)
single_patients_blood_tests_schema = PatientBloodTestsSchema()
many_patients_blood_tests_schema = PatientBloodTestsSchema(many=True)


@patient_blood_tests_endpoints.route('/add_patient_blood_test', methods=['POST'])
def add_patient_blood_test() -> (dict, int):
    data = request.json if request.is_json else request.form
    patient_blood_test = PatientBloodTests(patient_nhs_number=data['patient_nhs_number'],
                                           blood_test=data['blood_test'],
                                           date_taken=datetime.fromtimestamp(data['date_taken']))
    db.session.add(patient_blood_test)
    db.session.commit()
    return single_patients_blood_tests_schema.jsonify(patient_blood_test), 201


@patient_blood_tests_endpoints.route('/get_patient_blood_tests/<string:nhs_number>', methods=['GET'])
def get_patient_blood_tests(nhs_number: str) -> (dict, int):
    patient_blood_tests = PatientBloodTests.query.filter_by(patient_nhs_number=nhs_number).all()
    return many_patients_blood_tests_schema.jsonify(patient_blood_tests), 200
