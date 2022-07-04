from flask import Blueprint, Response, jsonify, request

from common import json_commons, requests_commons
from controller import blood_test_controller, medication_blood_tests_controller, patient_blood_tests_controller, \
    prescription_controller

patient_endpoints = Blueprint('patient_endpoints', __name__)


@patient_endpoints.route('/add_patient', methods=['POST'])
def add_patient() -> (object, int):
    data = request.json if request.is_json else request.form
    response = requests_commons.post_and_check('http://127.0.0.1:5002/add_patient', data)
    return response.content, response.status_code


@patient_endpoints.route('/get_patient/<string:nhs_number>', methods=['GET'])
def get_patient(nhs_number: str) -> (object, int):
    response = requests_commons.get_and_check(f'http://127.0.0.1:5002/get_patient/{nhs_number}')
    response_json = response.json()
    blood_tests: Response = patient_blood_tests_controller.get_patient_blood_tests(nhs_number)
    response_json['blood_tests'] = json_commons.load_from_string(blood_tests[0].get_data())
    prescriptions: Response = prescription_controller.get_prescriptions(nhs_number)
    response_json['prescriptions'] = json_commons.load_from_string(prescriptions[0].get_data())
    missing_blood_tests_data = patient_blood_tests_controller.get_pending_blood_test(response_json["nhs_number"])[0].data
    missing_blood_tests = json_commons.load_from_string(missing_blood_tests_data)
    for prescription in response_json['prescriptions']:
        medication_blood_tests = medication_blood_tests_controller.get_medication_blood_tests(prescription['medication_name'])
        prescription['required_blood_tests'] = json_commons.load_from_string(medication_blood_tests[0].get_data())
        prescription["deliverable"] = True
        for required_blood_test in prescription['required_blood_tests']:
            for missing_blood_test in missing_blood_tests:
                if required_blood_test["medication"] == missing_blood_test["medication"] \
                        and required_blood_test["blood_test"] == missing_blood_test["blood_test"]:
                    prescription["deliverable"] = False
                    break

    return jsonify(response_json), 200
