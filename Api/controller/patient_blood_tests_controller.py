from datetime import datetime

from flask import Blueprint, jsonify, request

from common import json_commons, requests_commons
from controller import blood_test_controller, medication_blood_tests_controller, prescription_controller
from service import blood_test_service

patient_blood_tests_endpoints = Blueprint('patient_blood_test_endpoints', __name__)


@patient_blood_tests_endpoints.route('/add_patient_blood_test', methods=['POST'])
def add_patient_blood_test() -> (dict, int):
    data = request.json if request.is_json else request.form
    data["date_taken"] = datetime.now().timestamp()
    requests_commons.post_and_check('http://127.0.0.1:5002/add_patient_blood_test', data)
    return jsonify(data), 201


@patient_blood_tests_endpoints.route('/get_patient_blood_tests/<string:nhs_number>', methods=['GET'])
def get_patient_blood_tests(nhs_number: str) -> (dict, int):
    response = requests_commons.get_and_check(f'http://127.0.0.1:5002/get_patient_blood_tests/{nhs_number}')
    patient_blood_tests = response.json()
    for patient_blood_test in patient_blood_tests:
        patient_blood_test["blood_test"], resp_code = blood_test_controller.get_blood_test(patient_blood_test["blood_test"])
    return jsonify(patient_blood_tests), response.status_code


@patient_blood_tests_endpoints.route('/get_pending_blood_tests/<string:nhs_number>', methods=['GET'])
def get_pending_blood_test(nhs_number: str) -> (dict, int):
    prescriptions_data = prescription_controller.get_prescriptions(nhs_number)[0].data
    prescriptions = json_commons.load_from_string(prescriptions_data)
    pending_tests = []
    for prescription in prescriptions:
        # get medication-blood test
        medication_blood_tests_data = medication_blood_tests_controller.get_medication_blood_tests(prescription["medication_name"])[0].data
        medication_blood_tests = json_commons.load_from_string(medication_blood_tests_data)
        # get patient-blood test
        patient_blood_tests_data = get_patient_blood_tests(nhs_number)[0].data
        patient_blood_tests = json_commons.load_from_string(patient_blood_tests_data)

        for medication_blood_test in medication_blood_tests:
            last_date_tested = blood_test_service.get_last_date_tested(patient_blood_tests, medication_blood_test['blood_test'])
            if last_date_tested == datetime.min or blood_test_service.test_is_pending(last_date_tested, medication_blood_test['frequency_days']):
                blood_test_service.add_if_needed(pending_tests, medication_blood_test)

    return jsonify(pending_tests), 200
