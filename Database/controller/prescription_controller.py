from datetime import datetime

from flask import Blueprint, jsonify, request

from extensions import db
from models.patient_prescriptions import PatientPrescriptions, PatientPrescriptionsSchema

prescription_endpoints = Blueprint('prescription_endpoints', __name__)
single_prescription_schema = PatientPrescriptionsSchema()
many_prescriptions_schema = PatientPrescriptionsSchema(many=True)


@prescription_endpoints.route('/add_prescription', methods=['POST'])
def add_prescription() -> (dict, int):
    data = request.json if request.is_json else request.form
    new_prescription = PatientPrescriptions(patient_nhs_number=data['patient_nhs_number'],
                                            medication_name=data['medication_name'],
                                            first_dose=datetime.fromtimestamp(float(data['first_dose']) / 1000),
                                            days_frequency=data['days_frequency'],
                                            repetitions=data['repetitions'],
                                            end_date=datetime.fromtimestamp(float(data['end_date']) / 1000)
                                            )
    db.session.add(new_prescription)
    db.session.commit()
    return jsonify(msg='Prescription added'), 200


@prescription_endpoints.route('/get_patient_prescriptions/<string:nhs_number>', methods=['GET'])
def get_prescription(nhs_number: str) -> (object, int):
    patient_prescriptions: [PatientPrescriptions] = PatientPrescriptions.query.filter_by(patient_nhs_number=nhs_number)\
        .all()
    if patient_prescriptions:
        return many_prescriptions_schema.jsonify(patient_prescriptions), 200
    else:
        return jsonify(msg='No prescription found'), 404


@prescription_endpoints.route('/get_all_prescriptions', methods=['GET'])
def get_all_prescription() -> (object, int):
    prescriptions: [PatientPrescriptions] = PatientPrescriptions.query.all()
    return many_prescriptions_schema.jsonify(prescriptions), 200
