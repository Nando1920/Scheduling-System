from datetime import datetime

from flask import Blueprint, jsonify, request

from extensions import db
from models.patient_general_practice import PatientGeneralPractice, PatientGeneralPracticeSchema

patient_general_practice_endpoints = Blueprint('patient_general_practice_endpoints', __name__)
patient_general_practice_schema = PatientGeneralPracticeSchema()


@patient_general_practice_endpoints.route('/get_patient_general_practice/<string:nhs_number>', methods=['GET'])
def get_patient_general_practice(nhs_number: str) -> (dict, int):
    newest_gp = PatientGeneralPractice.query.filter_by(patient=nhs_number)\
                                            .order_by(PatientGeneralPractice.from_date.desc())\
                                            .first()
    if newest_gp:
        return patient_general_practice_schema.jsonify(newest_gp), 200
    else:
        return jsonify(msg='Could not find a registered GP for that patient'), 404


@patient_general_practice_endpoints.route('/add_patient_general_practice', methods=['POST'])
def add_patient_general_practice() -> (dict, int):
    data = request.json if request.is_json else request.form
    new_gp = PatientGeneralPractice(patient=data['nhs_number'],
                                    general_practice=data['gp_id'],
                                    from_date=datetime.fromisoformat(data['time_from']))
    db.session.add(new_gp)
    db.session.commit()
    return patient_general_practice_schema.jsonify(new_gp), 200