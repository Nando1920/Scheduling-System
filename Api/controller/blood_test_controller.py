from flask import Blueprint, jsonify, request

from common import requests_commons

blood_tests_endpoints = Blueprint('blood_tests_endpoints', __name__)


@blood_tests_endpoints.route('/add_blood_test', methods=['POST'])
def add_blood_test() -> (dict, int):
    data = request.json if request.is_json else request.form
    try:
        requests_commons.get_and_check(f'http://127.0.0.1:5002/get_blood_test/{data["blood_test_type"]}')
        return jsonify(msg='Blood test already exists'), 409
    except ValueError:
        response = requests_commons.post_and_check(f'http://127.0.0.1:5002/add_blood_test', data)
        return response.json(), 201


@blood_tests_endpoints.route('/get_blood_test/<string:blood_test_type>', methods=['GET'])
def get_blood_test(blood_test_type: str) -> (dict, int):
    response = requests_commons.get_and_check(f'http://127.0.0.1:5002/get_blood_test/{blood_test_type}')
    return response.json(), 200
