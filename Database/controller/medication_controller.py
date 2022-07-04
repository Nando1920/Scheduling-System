from flask import Blueprint, jsonify, request

from extensions import db
from models.medications import Medications, MedicationsSchema

medication_endpoints = Blueprint('medication_endpoints', __name__)
medication_schema = MedicationsSchema()


@medication_endpoints.route('/get_medication/<string:medication_name>', methods=['GET'])
def get_medication(medication_name: str) -> (dict, int):
    medication = Medications.query.filter_by(medication_name=medication_name).first()
    if medication:
        return medication_schema.jsonify(medication), 200
    else:
        return None, 404


@medication_endpoints.route('/add_medication', methods=['POST'])
def add_medication() -> (dict, int):
    data = request.json if request.is_json else request.form
    existing_patient = Medications.query.filter_by(medication_name=data['medication_name']).first()
    if not existing_patient:
        medication = Medications(
            medication_name=data['medication_name'],
            unit_of_measurement=data['unit_of_measurement'],
            amount=data['amount']
        )
        db.session.add(medication)
        db.session.commit()
        return medication_schema.jsonify(medication), 200
    return jsonify(msg='Medication already exist'), 400
