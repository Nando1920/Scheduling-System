from flask import Blueprint, jsonify, request

from common import requests_commons

pickups_endpoints = Blueprint('pickups_endpoints', __name__)


@pickups_endpoints.route('/add_pickup', methods=['POST'])
def add_new_pickup() -> (dict, int):
    data = request.json if request.is_json else request.form
    body = {
        'prescription': data['prescription'],
        'staff': data['staff'],
        'delivered_on': data['delivered_on']
    }
    response = requests_commons.post_and_check(f'127.0.0.1:5002/add_pickup', body)
    return jsonify(response.json()), response.status_code
